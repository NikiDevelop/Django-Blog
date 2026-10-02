import json
import posixpath
import re
import tempfile
from importlib import import_module
from pathlib import Path
from urllib.parse import unquote

from django.template import Context, Template
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .carga import cargar_contenido
from .contenido import MODULOS
from .exportar import Exportacion
from .rutas import ruta_relativa
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


class RutasTests(TestCase):
    def test_ruta_relativa(self):
        self.assertEqual(ruta_relativa('/ia-facil/', '/ia-facil/blog/x/'), '../../')
        self.assertEqual(ruta_relativa('/ia-facil/blog/', '/ia-facil/blog/'), './')
        self.assertEqual(ruta_relativa('/static/a.css', '/'), 'static/a.css')
        self.assertEqual(ruta_relativa('/a/b/?x=1', '/a/c/'), '../b/?x=1')
        self.assertEqual(ruta_relativa('/a/#ancla', '/a/b/'), '../#ancla')


class ExportacionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cargar_contenido()

    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.raiz = Path(self.carpeta.name) / 'web'
        self.exportacion = Exportacion(self.raiz, 'https://midominio.com/').ejecutar()

    def tearDown(self):
        self.carpeta.cleanup()

    def leer(self, ruta):
        return (self.raiz / ruta).read_text(encoding='utf-8')

    def test_genera_todas_las_paginas(self):
        esperadas = 1 + sum(6 + s.articulos.count() + s.comparativas.count() + s.productos.count()
                            for s in Sitio.objects.all())
        self.assertEqual(len(self.exportacion.paginas), esperadas)
        self.assertTrue((self.raiz / 'index.html').exists())
        self.assertTrue((self.raiz / 'ia-facil/blog/como-hacer-fotos-con-ia/index.html').exists())
        for archivo in ('404.html', '.htaccess', 'static/nichos/css/nichos.css', 'static/nichos/js/estatico.js'):
            self.assertTrue((self.raiz / archivo).exists(), archivo)

    def test_ningun_enlace_interno_roto(self):
        rotos = []
        for html in self.raiz.rglob('*.html'):
            pagina = '/' + html.parent.relative_to(self.raiz).as_posix().strip('.') + '/'
            for url in re.findall(r'(?:href|src|action)="([^"]*)"', html.read_text(encoding='utf-8')):
                if not url or re.match(r'^(https?:|data:|mailto:|#|\?)', url):
                    continue
                ruta = re.split(r'[?#]', url)[0]
                destino = posixpath.normpath(ruta if html.name == '404.html' else posixpath.join(pagina, ruta))
                archivo = self.raiz / unquote(destino).lstrip('/')
                if archivo.is_dir():
                    archivo /= 'index.html'
                if not archivo.exists():
                    rotos.append(f'{html.relative_to(self.raiz)} -> {url}')
        self.assertEqual(rotos, [])

    def test_enlaces_relativos_y_sin_restos_del_servidor(self):
        articulo = self.leer('ia-facil/blog/como-hacer-fotos-con-ia/index.html')
        self.assertIn('href="../../../static/nichos/css/nichos.css"', articulo)
        self.assertIn('<script src="../../../static/nichos/js/estatico.js"', articulo)
        self.assertNotIn('testserver', articulo)
        self.assertNotIn('href="/webs/', articulo)

    def test_canonical_sitemap_y_robots_con_dominio(self):
        self.assertIn('<link rel="canonical" href="https://midominio.com/ia-facil/">', self.leer('ia-facil/index.html'))
        sitemap = self.leer('sitemap.xml')
        self.assertIn('<loc>https://midominio.com/ia-facil/blog/como-hacer-fotos-con-ia/</loc>', sitemap)
        self.assertNotIn('/buscar/', sitemap)
        self.assertIn('Sitemap: https://midominio.com/sitemap.xml', self.leer('robots.txt'))

    def test_pagina_404_con_enlaces_desde_la_raiz(self):
        pagina = self.leer('404.html')
        self.assertIn('Esta página no existe', pagina)
        self.assertIn('href="/static/nichos/css/nichos.css"', pagina)
        self.assertNotIn('rel="canonical"', pagina)

    def test_buscador_estatico_con_indice_relativo(self):
        pagina = self.leer('bolsillo-listo/buscar/index.html')
        indice = json.loads(re.search(r'<script id="indice-busqueda" type="application/json">(.*?)</script>',
                                      pagina, re.S).group(1))
        urls = {e['titulo']: e['url'] for e in indice}
        self.assertEqual(urls['Amortizar hipoteca: ¿reducir plazo o cuota? Ejemplo con números'],
                         '../blog/amortizar-plazo-o-cuota/')
        self.assertTrue(all(e['url'].startswith('../') for e in indice))

    def test_la_version_django_no_cambia(self):
        respuesta = self.client.get(reverse('nichos:buscar', args=['bolsillo-listo']))
        self.assertNotContains(respuesta, 'indice-busqueda')
        self.assertNotContains(respuesta, 'estatico.js')
