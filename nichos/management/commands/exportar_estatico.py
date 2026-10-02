import re
import shutil
import unicodedata
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from nichos.exportar import Exportacion
from nichos.models import Sitio


def sin_tildes(texto):
    return unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()


class Command(BaseCommand):
    help = ('Genera las webs en HTML estático para subirlas a cualquier hosting, por ejemplo al public_html '
            'de Hostinger. Por defecto, todas juntas con una portada; con --separadas, una carpeta y un .zip '
            'por web («IA Facil v.1»…).')

    def add_arguments(self, parser):
        parser.add_argument('--dominio', help='URL pública, p. ej. https://midominio.com (añade sitemap.xml, '
                                              'robots.txt y enlaces canónicos). Solo para la exportación conjunta')
        parser.add_argument('--separadas', action='store_true',
                            help='Una web independiente por carpeta, con su inicio en la raíz')
        parser.add_argument('--version-web', default='1',
                            help='Versión para el nombre de las carpetas: 1 -> «IA Facil v.1» (por defecto 1)')
        parser.add_argument('--salida', default=str(Path(settings.BASE_DIR) / 'publicar'),
                            help='Carpeta donde se genera el resultado (por defecto, publicar/)')

    def handle(self, *args, **options):
        dominio = options['dominio']
        if dominio and not dominio.startswith(('http://', 'https://')):
            raise CommandError('El dominio debe empezar por https:// (por ejemplo, https://midominio.com)')
        if dominio and options['separadas']:
            raise CommandError('--dominio solo vale para la exportación conjunta: cada web separada tendrá el suyo')

        try:
            if options['separadas']:
                self.exportar_separadas(Path(options['salida']), re.sub(r'^v\.?', '', options['version_web']))
            else:
                self.exportar_juntas(Path(options['salida']), dominio)
        except RuntimeError as error:
            raise CommandError(error)

    def exportar_juntas(self, salida, dominio):
        exportacion = Exportacion(salida / 'webs-de-tendencias', dominio).ejecutar()
        archivo_zip = exportacion.comprimir(salida / 'webs-de-tendencias')
        self.stdout.write(f'{len(exportacion.paginas)} páginas generadas en {exportacion.destino}')
        if not dominio:
            self.stdout.write('Sin --dominio no se generan sitemap.xml, robots.txt ni enlaces canónicos.')
        self.stdout.write(self.style.SUCCESS(f'Listo para subir: {archivo_zip}'))

    def exportar_separadas(self, salida, version):
        carpeta = salida / f'Webs v.{version}'
        if carpeta.exists():
            shutil.rmtree(carpeta)
        for sitio in Sitio.objects.filter(activo=True):
            nombre = f'{sin_tildes(sitio.nombre)} v.{version}'
            exportacion = Exportacion(carpeta / nombre, sitio=sitio).ejecutar()
            # El .zip lleva los archivos en la raíz: al extraerlo se crea la carpeta con el nombre de la web
            archivo_zip = exportacion.comprimir(carpeta / nombre)
            self.stdout.write(f'{sitio.icono} {nombre}: {len(exportacion.paginas)} páginas -> {Path(archivo_zip).name}')
        self.stdout.write(self.style.SUCCESS(f'Listo en {carpeta}'))
