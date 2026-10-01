from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Articulo, Comparativa, Producto, Sitio


class SitiosSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Sitio.objects.filter(activo=True)


class SeccionesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6
    secciones = ['blog', 'comparativas', 'tendencias', 'productos']

    def items(self):
        return [(s, seccion) for s in Sitio.objects.filter(activo=True).values_list('slug', flat=True)
                for seccion in self.secciones]

    def location(self, item):
        sitio, seccion = item
        return reverse(f'nichos:{seccion}', args=[sitio])


class ArticulosSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Articulo.objects.filter(publicado=True, sitio__activo=True).select_related('sitio')

    def lastmod(self, obj):
        return obj.fecha_publicacion


class ComparativasSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Comparativa.objects.filter(publicado=True, sitio__activo=True).select_related('sitio')

    def lastmod(self, obj):
        return obj.fecha_publicacion


class ProductosSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Producto.objects.filter(publicado=True, sitio__activo=True).select_related('sitio')


sitemaps = {
    'sitios': SitiosSitemap,
    'secciones': SeccionesSitemap,
    'articulos': ArticulosSitemap,
    'comparativas': ComparativasSitemap,
    'productos': ProductosSitemap,
}
