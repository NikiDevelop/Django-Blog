from django.conf import settings

from .models import Sitio


def red_sitios(request):
    return {
        # Queryset perezoso: solo consulta la base de datos si la plantilla lo usa (pie de página)
        'red_sitios': Sitio.objects.filter(activo=True),
        # True mientras se genera la versión en HTML estático (ver exportar_estatico)
        'estatico': getattr(settings, 'NICHOS_ESTATICO', False),
    }
