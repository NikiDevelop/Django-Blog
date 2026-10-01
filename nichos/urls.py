from django.urls import path

from . import views

app_name = 'nichos'

urlpatterns = [
    path('', views.portada, name='portada'),
    path('<slug:sitio>/', views.inicio, name='inicio'),
    path('<slug:sitio>/blog/', views.blog, name='blog'),
    path('<slug:sitio>/blog/<slug:slug>/', views.articulo, name='articulo'),
    path('<slug:sitio>/comparativas/', views.comparativas, name='comparativas'),
    path('<slug:sitio>/comparativas/<slug:slug>/', views.comparativa, name='comparativa'),
    path('<slug:sitio>/tendencias/', views.tendencias, name='tendencias'),
    path('<slug:sitio>/productos/', views.productos, name='productos'),
    path('<slug:sitio>/productos/<slug:slug>/', views.producto, name='producto'),
    path('<slug:sitio>/buscar/', views.buscar, name='buscar'),
]
