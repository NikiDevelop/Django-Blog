from django.core.management.base import BaseCommand

from nichos.carga import cargar_contenido


class Command(BaseCommand):
    help = 'Crea o actualiza las 5 webs de tendencias con su blog, comparativas, tendencias y productos.'

    def add_arguments(self, parser):
        parser.add_argument('sitios', nargs='*', help='Slugs de las webs a cargar (por defecto, todas)')

    def handle(self, *args, **options):
        sitios = cargar_contenido(solo=options['sitios'] or None)
        for sitio in sitios:
            self.stdout.write(
                f'{sitio.icono} {sitio.nombre}: {sitio.articulos.count()} artículos, '
                f'{sitio.comparativas.count()} comparativas, {sitio.tendencias.count()} tendencias, '
                f'{sitio.productos.count()} productos'
            )
        self.stdout.write(self.style.SUCCESS(f'{len(sitios)} webs cargadas. Visítalas en /webs/'))
