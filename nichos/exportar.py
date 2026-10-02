"""Genera una copia en HTML estático de las webs, lista para subir a cualquier hosting.

Cada página se renderiza con Django, los enlaces internos pasan a ser relativos (funciona en la raíz
de un dominio o en una subcarpeta) y se copian solo los estáticos que se usan.

- Todas juntas: la portada de /webs/ queda en la raíz y cada web en su carpeta (/ia-facil/, /vida-longeva/…).
- Una web sola (`sitio`): su inicio queda en la raíz (/blog/, /productos/…), lista para su propio dominio.
"""
import logging
import re
import shutil
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

from django.contrib.staticfiles import finders
from django.test import Client
from django.test.utils import override_settings
from django.urls import reverse

from .models import Sitio
from .rutas import ruta_relativa

ENLACE = re.compile(r'(href|src|action)="(/(?!/)[^"]*)"')
CANONICAL = re.compile(r'\n?\s*<link rel="canonical" href="http://testserver(/[^"]*)">')
SECCIONES = ('inicio', 'blog', 'comparativas', 'tendencias', 'productos', 'buscar')

HTACCESS = """# Generado por exportar_estatico
ErrorDocument 404 /404.html
Options -Indexes
DirectoryIndex index.html

# Cuando el certificado SSL esté activo en Hostinger, quita las almohadillas para forzar HTTPS
# (o activa «Forzar HTTPS» en hPanel):
# RewriteEngine On
# RewriteCond %{HTTPS} !=on
# RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "DENY"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>

<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml
</IfModule>

<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 7 days"
    ExpiresByType application/javascript "access plus 7 days"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>
"""


class Exportacion:
    """Exporta todas las webs juntas (portada en la raíz) o, con `sitio`, una sola web en la raíz."""

    def __init__(self, destino, dominio=None, sitio=None):
        self.destino = Path(destino)
        self.dominio = dominio.rstrip('/') if dominio else None
        self.sitio = sitio
        self.prefijo = reverse('nichos:inicio', args=[sitio.slug]) if sitio else reverse('nichos:portada')
        self.estaticos = set()
        self.paginas = []

    def ruta_publica(self, ruta):
        """Ruta en el sitio publicado: /webs/ia-facil/blog/ -> /ia-facil/blog/, o /blog/ si se exporta solo esa web."""
        if ruta.startswith(self.prefijo):
            return '/' + ruta[len(self.prefijo):]
        if ruta.startswith('/static/'):
            return ruta
        raise RuntimeError(f'Enlace a una página que no forma parte de la exportación: {ruta}')

    def urls(self):
        urls = [] if self.sitio else [self.prefijo]
        for sitio in [self.sitio] if self.sitio else Sitio.objects.filter(activo=True):
            urls += [reverse(f'nichos:{seccion}', args=[sitio.slug]) for seccion in SECCIONES]
            urls += [a.get_absolute_url() for a in sitio.articulos.filter(publicado=True)]
            urls += [c.get_absolute_url() for c in sitio.comparativas.filter(publicado=True)]
            urls += [p.get_absolute_url() for p in sitio.productos.filter(publicado=True)]
        return urls

    def reescribir(self, html, pagina, absolutas=False):
        """Adapta los enlaces de una página que se publicará en la ruta `pagina`."""
        def enlace(coincidencia):
            atributo, ruta = coincidencia.groups()
            if ruta.startswith('/static/'):
                self.estaticos.add(re.split(r'[?#]', ruta)[0])
            publica = self.ruta_publica(ruta)
            return f'{atributo}="{publica if absolutas else ruta_relativa(publica, pagina)}"'

        def canonical(coincidencia):
            if not self.dominio or absolutas:
                return ''
            return f'\n  <link rel="canonical" href="{self.dominio}{self.ruta_publica(coincidencia.group(1))}">'

        return CANONICAL.sub(canonical, ENLACE.sub(enlace, html))

    def guardar(self, ruta, contenido):
        archivo = self.destino / ruta.lstrip('/')
        archivo.parent.mkdir(parents=True, exist_ok=True)
        archivo.write_text(contenido, encoding='utf-8')

    def ejecutar(self):
        if self.destino.exists():
            shutil.rmtree(self.destino)
        self.destino.mkdir(parents=True)

        # Sin paginación (todo en una página) y con los filtros y el buscador en el navegador
        with override_settings(NICHOS_ESTATICO=True, NICHOS_ESTATICO_INDEPENDIENTE=bool(self.sitio),
                               NICHOS_POR_PAGINA=10 ** 6, DEBUG=False,
                               ALLOWED_HOSTS=['testserver'], SECURE_SSL_REDIRECT=False):
            cliente = Client()
            for url in self.urls():
                respuesta = cliente.get(url)
                if respuesta.status_code != 200:
                    raise RuntimeError(f'{url} respondió {respuesta.status_code}')
                pagina = self.ruta_publica(url)
                self.guardar(pagina + 'index.html', self.reescribir(respuesta.content.decode(), pagina))
                self.paginas.append(pagina)

            # Se sirve en cualquier URL inexistente, así que sus enlaces van desde la raíz del dominio.
            # El 404 es intencionado: se silencia el aviso que Django escribe en el log.
            registro = logging.getLogger('django.request')
            nivel = registro.level
            registro.setLevel(logging.ERROR)
            try:
                respuesta = cliente.get(self.prefijo + 'pagina-que-no-existe/')
            finally:
                registro.setLevel(nivel)
            self.guardar('404.html', self.reescribir(respuesta.content.decode(), '/', absolutas=True))

        self.copiar_estaticos()
        self.guardar('.htaccess', HTACCESS)
        if self.dominio:
            self.guardar('sitemap.xml', self.sitemap())
            self.guardar('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {self.dominio}/sitemap.xml\n')
        return self

    def copiar_estaticos(self):
        for ruta in sorted(self.estaticos):
            origen = finders.find(ruta[len('/static/'):])
            if not origen:
                raise RuntimeError(f'No se encuentra el archivo estático {ruta}')
            destino = self.destino / ruta.lstrip('/')
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origen, destino)

    def sitemap(self):
        hoy = date.today().isoformat()
        entradas = ''.join(
            f'  <url><loc>{escape(self.dominio + pagina)}</loc><lastmod>{hoy}</lastmod></url>\n'
            for pagina in self.paginas if not pagina.endswith('/buscar/')
        )
        return ('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                f'{entradas}</urlset>\n')

    def comprimir(self, zip_sin_extension):
        return shutil.make_archive(str(zip_sin_extension), 'zip', root_dir=self.destino)
