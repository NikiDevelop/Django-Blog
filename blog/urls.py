from django.urls import path, include
from .views import home, cine, programacion, tecnologia, videojuegos, tutoriales, contacto, detallePost


app_name = 'blog'

#Importante en el campo name='' poner el nombre exacto al de la categoria 
#que hemos creado en nuestro panel de admin
urlpatterns = [
    path('', home, name='index'),
    path('cine/', cine, name='cine'),
    path('programacion/', programacion, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('tutoriales/', tutoriales, name='tutoriales'),   
    path('contacto/', tutoriales, name='contacto'), 
    path('post/<int:post_id>/', detallePost, name='post_detalle'),
   

]
