
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blog.urls', namespace='blog')),
    path('cine/', include('blog.urls', namespace='cine')),
    path('programacion/', include('blog.urls', namespace='programacion')),
    path('tecnologia/', include('blog.urls', namespace='tecnologia')),
    path('videojuegos/', include('blog.urls', namespace='videojuegos')),
    path('tutoriales/', include('blog.urls', namespace='tutoriales')),
    path('contacto/', include('blog.urls', namespace='contacto')),
    path('post/<int:pk>/', include('blog.urls', namespace='post_detalle')),
    path('categoria/<int:pk>/', include('blog.urls', namespace='categoria')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
