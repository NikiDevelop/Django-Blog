from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoría', max_length = 100, null=False, blank=False)
    estado = models.BooleanField('estado', default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length = 100, null=False, blank=False)
    apellidos = models.CharField( max_length = 255, null=False, blank=False)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)
    
#Creamos los campos que queremos que tenga nuestro post
#En el caso del tamaño de los campos (max_length) yo he decidido usar estos valores
#pero en contenido no hay límite por ejemplo

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    slug = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=250, blank=False, null=False)

    #RichTextField es muy interesante para poder personalizar el texto a tu manera y 
    #poder subir imagenes, así como poner links desde nuestro panel de administrador
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="images/")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo