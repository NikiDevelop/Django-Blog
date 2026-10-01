"""Carga el contenido inicial de las webs desde los módulos de nichos/contenido/.

Es idempotente: vuelve a ejecutarse sin duplicar nada, porque busca cada
elemento por (sitio, slug) y actualiza sus campos.
"""
from datetime import date, timedelta
from importlib import import_module

from django.db import transaction

from .contenido import MODULOS
from .models import Articulo, Comparativa, Producto, Sitio, Tendencia

# Fecha de referencia para escalonar las publicaciones del contenido inicial
FECHA_BASE = date(2026, 10, 1)


def _fecha(datos, posicion):
    return datos.pop('fecha', None) or FECHA_BASE - timedelta(days=3 * posicion)


@transaction.atomic
def cargar_sitio(modulo):
    datos_sitio = dict(modulo.SITIO)
    slug = datos_sitio.pop('slug')
    sitio, _ = Sitio.objects.update_or_create(slug=slug, defaults=datos_sitio)

    for posicion, datos in enumerate(modulo.ARTICULOS):
        datos = dict(datos)
        datos['fecha_publicacion'] = _fecha(datos, posicion)
        Articulo.objects.update_or_create(sitio=sitio, slug=datos.pop('slug'), defaults=datos)

    for datos in modulo.PRODUCTOS:
        datos = dict(datos)
        Producto.objects.update_or_create(sitio=sitio, slug=datos.pop('slug'), defaults=datos)

    for posicion, datos in enumerate(modulo.COMPARATIVAS):
        datos = dict(datos)
        slugs_productos = datos.pop('productos', [])
        datos['fecha_publicacion'] = _fecha(datos, posicion)
        comparativa, _ = Comparativa.objects.update_or_create(sitio=sitio, slug=datos.pop('slug'), defaults=datos)
        comparativa.productos.set(Producto.objects.filter(sitio=sitio, slug__in=slugs_productos))

    for orden, datos in enumerate(modulo.TENDENCIAS):
        datos = dict(datos)
        slug_articulo = datos.pop('articulo', None)
        datos['articulo'] = Articulo.objects.filter(sitio=sitio, slug=slug_articulo).first() if slug_articulo else None
        datos.setdefault('orden', orden)
        Tendencia.objects.update_or_create(sitio=sitio, slug=datos.pop('slug'), defaults=datos)

    return sitio


def cargar_contenido(solo=None):
    """Carga todas las webs, o solo las indicadas por slug en `solo`."""
    sitios = []
    for nombre in MODULOS:
        modulo = import_module(f'nichos.contenido.{nombre}')
        if solo and modulo.SITIO['slug'] not in solo:
            continue
        sitios.append(cargar_sitio(modulo))
    return sitios
