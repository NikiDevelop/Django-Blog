from django.contrib import admin

from .models import Articulo, Comparativa, Producto, Sitio, Tendencia


@admin.register(Sitio)
class SitioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nicho', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    prepopulated_fields = {'slug': ['nombre']}


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sitio', 'categoria', 'fecha_publicacion', 'destacado', 'publicado']
    list_filter = ['sitio', 'categoria', 'destacado', 'publicado']
    search_fields = ['titulo', 'resumen', 'palabra_clave']
    prepopulated_fields = {'slug': ['titulo']}


@admin.register(Comparativa)
class ComparativaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sitio', 'ganador', 'fecha_publicacion', 'publicado']
    list_filter = ['sitio', 'publicado']
    search_fields = ['titulo', 'resumen']
    prepopulated_fields = {'slug': ['titulo']}
    filter_horizontal = ['productos']


@admin.register(Tendencia)
class TendenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'sitio', 'estado', 'dato', 'fuente', 'orden']
    list_filter = ['sitio', 'estado']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ['nombre']}


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'sitio', 'categoria', 'puntuacion', 'precio_orientativo', 'destacado', 'publicado']
    list_filter = ['sitio', 'categoria', 'destacado', 'publicado']
    search_fields = ['nombre', 'marca', 'resumen']
    prepopulated_fields = {'slug': ['nombre']}
