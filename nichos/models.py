from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

color_hex = RegexValidator(r'^#[0-9a-fA-F]{6}$', 'Usa un color hexadecimal, p. ej. #2f89fc')


# Cada Sitio es una web independiente de un nicho en tendencia.
# Todo su contenido (blog, comparativas, tendencias y productos) cuelga de él.
class Sitio(models.Model):
    nombre = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    eslogan = models.CharField(max_length=160)
    descripcion = models.TextField(help_text='Texto de presentación de la web')
    nicho = models.CharField(max_length=120, help_text='Temática principal, p. ej. "Inteligencia artificial"')
    icono = models.CharField(max_length=8, help_text='Emoji que identifica la web')
    color_primario = models.CharField(max_length=7, default='#2f89fc', validators=[color_hex])
    color_secundario = models.CharField(max_length=7, default='#0f172a', validators=[color_hex])
    # Por qué existe esta web: datos de búsqueda que justifican el nicho
    por_que = models.TextField('Por qué es tendencia', help_text='HTML con los datos de la investigación')
    fuentes = models.JSONField(default=list, blank=True, help_text='Lista de {"titulo": ..., "url": ...}')
    orden = models.PositiveSmallIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = 'Sitios'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('nichos:inicio', args=[self.slug])


class Articulo(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='articulos')
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField(help_text='HTML del artículo')
    categoria = models.CharField(max_length=60)
    palabra_clave = models.CharField('Palabra clave SEO', max_length=120, blank=True)
    icono = models.CharField(max_length=8, blank=True)
    minutos_lectura = models.PositiveSmallIntegerField(default=5)
    destacado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(default=timezone.localdate)

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-destacado', '-fecha_publicacion', 'titulo']
        constraints = [
            models.UniqueConstraint(fields=['sitio', 'slug'], name='articulo_slug_unico_por_sitio'),
        ]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('nichos:articulo', args=[self.sitio.slug, self.slug])


class Producto(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140)
    marca = models.CharField(max_length=80, blank=True)
    categoria = models.CharField(max_length=60)
    icono = models.CharField(max_length=8, blank=True)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField(blank=True, help_text='HTML del análisis')
    ideal_para = models.CharField(max_length=160, blank=True)
    precio_orientativo = models.CharField(max_length=60, blank=True)
    # Valoración editorial (0-10) basada en especificaciones y relación calidad/precio
    puntuacion = models.DecimalField(max_digits=3, decimal_places=1, default=0,
                                     validators=[MinValueValidator(0), MaxValueValidator(10)])
    pros = models.JSONField(default=list, blank=True)
    contras = models.JSONField(default=list, blank=True)
    especificaciones = models.JSONField(default=dict, blank=True)
    enlace = models.URLField('Enlace de compra o afiliado', blank=True)
    destacado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-destacado', '-puntuacion', 'nombre']
        constraints = [
            models.UniqueConstraint(fields=['sitio', 'slug'], name='producto_slug_unico_por_sitio'),
        ]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('nichos:producto', args=[self.sitio.slug, self.slug])


class Comparativa(models.Model):
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='comparativas')
    titulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160)
    resumen = models.CharField(max_length=300)
    introduccion = models.TextField(help_text='HTML antes de la tabla')
    # La tabla es genérica para poder comparar productos, opciones o estrategias:
    # columnas = ["Opción A", "Opción B"], filas = [["Criterio", "valor A", "valor B"], ...]
    columnas = models.JSONField(default=list)
    filas = models.JSONField(default=list)
    ganador = models.CharField(max_length=120, blank=True)
    veredicto = models.TextField(help_text='HTML con la conclusión')
    productos = models.ManyToManyField(Producto, blank=True, related_name='comparativas')
    icono = models.CharField(max_length=8, blank=True)
    destacado = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(default=timezone.localdate)

    class Meta:
        verbose_name = 'Comparativa'
        verbose_name_plural = 'Comparativas'
        ordering = ['-destacado', '-fecha_publicacion', 'titulo']
        constraints = [
            models.UniqueConstraint(fields=['sitio', 'slug'], name='comparativa_slug_unico_por_sitio'),
        ]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('nichos:comparativa', args=[self.sitio.slug, self.slug])


class Tendencia(models.Model):
    EMERGENTE = 'emergente'
    EN_AUGE = 'en_auge'
    CONSOLIDADA = 'consolidada'
    ESTADOS = [
        (EMERGENTE, 'Emergente'),
        (EN_AUGE, 'En auge'),
        (CONSOLIDADA, 'Consolidada'),
    ]

    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='tendencias')
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    descripcion = models.TextField(help_text='HTML breve')
    estado = models.CharField(max_length=20, choices=ESTADOS, default=EN_AUGE)
    # Solo datos publicados por la fuente; se deja vacío si no hay cifra
    dato = models.CharField('Dato clave', max_length=80, blank=True, help_text='p. ej. "+4.300 % en búsquedas"')
    fuente = models.CharField(max_length=120, blank=True)
    fuente_url = models.URLField(blank=True)
    icono = models.CharField(max_length=8, blank=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='tendencias')
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Tendencia'
        verbose_name_plural = 'Tendencias'
        ordering = ['orden', 'nombre']
        constraints = [
            models.UniqueConstraint(fields=['sitio', 'slug'], name='tendencia_slug_unico_por_sitio'),
        ]

    def __str__(self):
        return self.nombre
