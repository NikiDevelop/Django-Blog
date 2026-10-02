from importlib import import_module

from django.template import Context, Template
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .carga import cargar_contenido
from .contenido import MODULOS
from .models import Articulo, Comparativa, Producto, Sitio, Tendencia


class ContenidoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cargar_contenido()

    def test_carga_las_cinco_webs_con_todas_las_secciones(self):
        self.assertEqual(Sitio.objects.count(), 5)
        for sitio in Sitio.objects.all():
            with self.subTest(sitio=sitio.slug):
                self.assertGreaterEqual(sitio.articulos.count(), 4)
                self.assertGreaterEqual(sitio.comparativas.count(), 2)
                self.assertGreaterEqual(sitio.tendencias.count(), 5)
                self.assertGreaterEqual(sitio.productos.count(), 5)
                self.assertTrue(sitio.fuentes)

    def test_la_carga_es_idempotente(self):
        totales = [m.objects.count() for m in (Sitio, Articulo, Comparativa, Tendencia, Producto)]
        cargar_contenido()
        self.assertEqual(totales, [m.objects.count() for m in (Sitio, Articulo, Comparativa, Tendencia, Producto)])

    def test_tablas_de_comparativas_coherentes(self):
        for comparativa in Comparativa.objects.all():
            with self.subTest(comparativa=comparativa.slug):
                if comparativa.ganador:
                    self.assertIn(comparativa.ganador, comparativa.columnas)
                for fila in comparativa.filas:
                    self.assertEqual(len(fila), len(comparativa.columnas) + 1)

    def test_las_referencias_del_contenido_existen(self):
        # Un slug mal escrito en contenido/ se ignoraría en silencio al cargar
        for nombre in MODULOS:
            modulo = import_module(f'nichos.contenido.{nombre}')
            sitio = Sitio.objects.get(slug=modulo.SITIO['slug'])
            for datos in modulo.COMPARATIVAS:
                comparativa = sitio.comparativas.get(slug=datos['slug'])
                self.assertEqual(set(comparativa.productos.values_list('slug', flat=True)),
                                 set(datos.get('productos', [])), comparativa.slug)
            for datos in modulo.TENDENCIAS:
                if datos.get('articulo'):
                    tendencia = sitio.tendencias.get(slug=datos['slug'])
                    self.assertEqual(getattr(tendencia.articulo, 'slug', None), datos['articulo'], tendencia.slug)

    def test_datos_validos_segun_el_modelo(self):
        for modelo in (Sitio, Articulo, Comparativa, Tendencia, Producto):
            for obj in modelo.objects.all():
                with self.subTest(obj=str(obj)):
                    obj.full_clean()

    def test_tendencias_enlazan_con_articulos_del_mismo_sitio(self):
        for tendencia in Tendencia.objects.exclude(articulo=None):
            self.assertEqual(tendencia.articulo.sitio_id, tendencia.sitio_id)


class VistasTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cargar_contenido()

    def test_portada_lista_las_webs(self):
        respuesta = self.client.get(reverse('nichos:portada'))
        self.assertEqual(respuesta.status_code, 200)
        for sitio in Sitio.objects.all():
            self.assertContains(respuesta, sitio.nombre)

    def test_todas_las_paginas_responden(self):
        for sitio in Sitio.objects.all():
            urls = [reverse(f'nichos:{s}', args=[sitio.slug])
                    for s in ('inicio', 'blog', 'comparativas', 'tendencias', 'productos', 'buscar')]
            urls += [obj.get_absolute_url() for obj in sitio.articulos.all()]
            urls += [obj.get_absolute_url() for obj in sitio.comparativas.all()]
            urls += [obj.get_absolute_url() for obj in sitio.productos.all()]
            for url in urls:
                with self.subTest(url=url):
                    self.assertEqual(self.client.get(url).status_code, 200)

    def test_sitio_inexistente_o_inactivo_da_404(self):
        self.assertEqual(self.client.get('/webs/no-existe/').status_code, 404)
        sitio = Sitio.objects.get(slug='ia-facil')
        sitio.activo = False
        sitio.save()
        self.assertEqual(self.client.get(sitio.get_absolute_url()).status_code, 404)

    def test_articulo_no_publicado_da_404(self):
        articulo = Articulo.objects.first()
        articulo.publicado = False
        articulo.save()
        self.assertEqual(self.client.get(articulo.get_absolute_url()).status_code, 404)

    def test_contenido_de_un_sitio_no_aparece_en_otro(self):
        articulo = Articulo.objects.get(sitio__slug='bolsillo-listo', slug='amortizar-plazo-o-cuota')
        url = reverse('nichos:articulo', args=['ia-facil', articulo.slug])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_comparativa_resalta_al_ganador(self):
        comparativa = Comparativa.objects.get(slug='mejores-estaciones-de-energia-portatiles')
        respuesta = self.client.get(comparativa.get_absolute_url())
        self.assertEqual(respuesta.context['ganador_idx'], comparativa.columnas.index('Anker SOLIX C1000'))
        self.assertContains(respuesta, 'es-ganador')

    def test_buscador_del_sitio(self):
        respuesta = self.client.get(reverse('nichos:buscar', args=['bolsillo-listo']), {'q': 'Euríbor'})
        self.assertContains(respuesta, 'Euríbor en 2026')
        # La búsqueda no mezcla resultados de otras webs
        self.assertNotContains(respuesta, 'Cómo hacer fotos con IA')

    def test_blog_filtra_por_categoria_y_texto(self):
        url = reverse('nichos:blog', args=['vida-longeva'])
        respuesta = self.client.get(url, {'categoria': 'Sueño'})
        self.assertEqual([a.slug for a in respuesta.context['articulos']], ['dormir-mejor-ciencia'])
        respuesta = self.client.get(url, {'q': 'creatina'})
        self.assertIn('creatina-para-que-sirve', [a.slug for a in respuesta.context['articulos']])

    def test_tendencias_filtran_por_estado(self):
        respuesta = self.client.get(reverse('nichos:tendencias', args=['vida-longeva']), {'estado': 'emergente'})
        estados = {t.estado for t in respuesta.context['tendencias']}
        self.assertEqual(estados, {Tendencia.EMERGENTE})

    def test_productos_filtran_por_categoria(self):
        respuesta = self.client.get(reverse('nichos:productos', args=['casa-autonoma']),
                                    {'categoria': 'Kit de emergencia'})
        self.assertTrue(respuesta.context['productos'])
        self.assertTrue(all(p.categoria == 'Kit de emergencia' for p in respuesta.context['productos']))

    def test_pagina_404_propia(self):
        respuesta = self.client.get('/webs/no-existe/')
        self.assertContains(respuesta, 'Esta página no existe', status_code=404)

    def test_robots_txt_apunta_al_sitemap(self):
        respuesta = self.client.get('/robots.txt')
        self.assertEqual(respuesta['Content-Type'], 'text/plain')
        self.assertContains(respuesta, 'Disallow: /admin/')
        self.assertContains(respuesta, 'Sitemap: http://testserver/sitemap.xml')

    def test_salud_responde_ok(self):
        respuesta = self.client.get('/salud/')
        self.assertContains(respuesta, 'ok')
        self.assertIn('no-cache', respuesta['Cache-Control'])

    def test_sitemap_incluye_articulos(self):
        respuesta = self.client.get('/sitemap.xml')
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '/webs/ia-facil/blog/como-hacer-fotos-con-ia/')


class EtiquetasTests(TestCase):
    def test_url_con_cambia_solo_los_parametros_indicados(self):
        peticion = RequestFactory().get('/webs/x/blog/', {'q': 'ia', 'page': '2'})
        plantilla = Template('{% load nichos_extras %}{% url_con page=None categoria="Guías" %}')
        resultado = plantilla.render(Context({'request': peticion}))
        self.assertIn('q=ia', resultado)
        self.assertIn('categoria=Gu%C3%ADas', resultado)
        self.assertNotIn('page=', resultado)

    def test_porcentaje(self):
        plantilla = Template('{% load nichos_extras %}{{ nota|porcentaje }}')
        self.assertEqual(plantilla.render(Context({'nota': '8.7'})), '87')
        self.assertEqual(plantilla.render(Context({'nota': None})), '0')
