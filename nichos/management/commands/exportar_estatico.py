from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from nichos.exportar import Exportacion


class Command(BaseCommand):
    help = ('Genera las webs en HTML estático (carpeta y .zip) para subirlas a cualquier hosting, '
            'por ejemplo al public_html de Hostinger.')

    def add_arguments(self, parser):
        parser.add_argument('--dominio', help='URL pública, p. ej. https://midominio.com (añade sitemap.xml, '
                                              'robots.txt y enlaces canónicos)')
        parser.add_argument('--salida', default=str(Path(settings.BASE_DIR) / 'publicar'),
                            help='Carpeta donde se genera el resultado (por defecto, publicar/)')

    def handle(self, *args, **options):
        dominio = options['dominio']
        if dominio and not dominio.startswith(('http://', 'https://')):
            raise CommandError('El dominio debe empezar por https:// (por ejemplo, https://midominio.com)')

        salida = Path(options['salida'])
        try:
            exportacion = Exportacion(salida / 'webs-de-tendencias', dominio).ejecutar()
        except RuntimeError as error:
            raise CommandError(error)
        archivo_zip = exportacion.comprimir(salida / 'webs-de-tendencias')

        self.stdout.write(f'{len(exportacion.paginas)} páginas generadas en {exportacion.destino}')
        if not dominio:
            self.stdout.write('Sin --dominio no se generan sitemap.xml, robots.txt ni enlaces canónicos.')
        self.stdout.write(self.style.SUCCESS(f'Listo para subir: {archivo_zip}'))
