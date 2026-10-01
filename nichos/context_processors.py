from .models import Sitio


def red_sitios(request):
    # Queryset perezoso: solo consulta la base de datos si la plantilla lo usa (pie de página)
    return {'red_sitios': Sitio.objects.filter(activo=True)}
