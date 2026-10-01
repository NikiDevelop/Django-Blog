from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_con(context, **parametros):
    """Devuelve la querystring actual cambiando solo los parámetros indicados.

    Un valor vacío o None elimina el parámetro: {% url_con categoria=c page=None %}
    """
    query = context['request'].GET.copy()
    for clave, valor in parametros.items():
        if valor in (None, ''):
            query.pop(clave, None)
        else:
            query[clave] = valor
    return '?' + query.urlencode() if query else '?'


@register.filter
def porcentaje(puntuacion):
    """Convierte una nota sobre 10 en porcentaje para las barras de valoración."""
    try:
        return max(0, min(100, round(float(puntuacion) * 10)))
    except (TypeError, ValueError):
        return 0
