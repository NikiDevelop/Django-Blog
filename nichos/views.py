from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render

from .models import Articulo, Comparativa, Producto, Sitio, Tendencia


def _sitio(slug):
    return get_object_or_404(Sitio, slug=slug, activo=True)


def portada(request):
    # Página que agrupa las 5 webs de tendencias
    sitios = Sitio.objects.filter(activo=True).annotate(
        num_articulos=Count('articulos', filter=Q(articulos__publicado=True), distinct=True),
        num_comparativas=Count('comparativas', filter=Q(comparativas__publicado=True), distinct=True),
        num_productos=Count('productos', filter=Q(productos__publicado=True), distinct=True),
        num_tendencias=Count('tendencias', distinct=True),
    )
    return render(request, 'nichos/portada.html', {'sitios': sitios})


def inicio(request, sitio):
    sitio = _sitio(sitio)
    articulos = sitio.articulos.filter(publicado=True)
    contexto = {
        'sitio': sitio,
        'destacado': articulos.filter(destacado=True).first() or articulos.first(),
        'articulos': articulos[:6],
        'comparativas': sitio.comparativas.filter(publicado=True)[:3],
        'tendencias': sitio.tendencias.select_related('articulo__sitio')[:4],
        'productos': sitio.productos.filter(publicado=True)[:4],
    }
    return render(request, 'nichos/inicio.html', contexto)


def blog(request, sitio):
    sitio = _sitio(sitio)
    articulos = sitio.articulos.filter(publicado=True)
    categorias = articulos.order_by('categoria').values_list('categoria', flat=True).distinct()

    categoria = request.GET.get('categoria')
    if categoria:
        articulos = articulos.filter(categoria=categoria)

    #__icontains busca sin distinguir mayúsculas y minúsculas
    buscar = request.GET.get('q', '').strip()
    if buscar:
        articulos = articulos.filter(
            Q(titulo__icontains=buscar) | Q(resumen__icontains=buscar) | Q(contenido__icontains=buscar)
        )

    paginator = Paginator(articulos, 9)
    articulos = paginator.get_page(request.GET.get('page'))
    return render(request, 'nichos/blog.html', {
        'sitio': sitio,
        'articulos': articulos,
        'categorias': categorias,
        'categoria': categoria,
        'buscar': buscar,
    })


def articulo(request, sitio, slug):
    sitio = _sitio(sitio)
    articulo = get_object_or_404(Articulo, sitio=sitio, slug=slug, publicado=True)
    relacionados = sitio.articulos.filter(publicado=True).exclude(pk=articulo.pk)
    return render(request, 'nichos/articulo.html', {
        'sitio': sitio,
        'articulo': articulo,
        'relacionados': relacionados[:3],
        'productos': sitio.productos.filter(publicado=True)[:3],
        'tendencias': articulo.tendencias.all(),
    })


def comparativas(request, sitio):
    sitio = _sitio(sitio)
    return render(request, 'nichos/comparativas.html', {
        'sitio': sitio,
        'comparativas': sitio.comparativas.filter(publicado=True),
    })


def comparativa(request, sitio, slug):
    sitio = _sitio(sitio)
    comparativa = get_object_or_404(Comparativa, sitio=sitio, slug=slug, publicado=True)
    # Posición de la columna ganadora para resaltarla en la tabla
    ganador_idx = comparativa.columnas.index(comparativa.ganador) if comparativa.ganador in comparativa.columnas else -1
    return render(request, 'nichos/comparativa.html', {
        'sitio': sitio,
        'comparativa': comparativa,
        'ganador_idx': ganador_idx,
        'productos': comparativa.productos.filter(publicado=True),
        'otras': sitio.comparativas.filter(publicado=True).exclude(pk=comparativa.pk)[:3],
    })


def tendencias(request, sitio):
    sitio = _sitio(sitio)
    tendencias = sitio.tendencias.select_related('articulo__sitio')
    estado = request.GET.get('estado')
    if estado in dict(Tendencia.ESTADOS):
        tendencias = tendencias.filter(estado=estado)
    return render(request, 'nichos/tendencias.html', {
        'sitio': sitio,
        'tendencias': tendencias,
        'estados': Tendencia.ESTADOS,
        'estado': estado,
    })


def productos(request, sitio):
    sitio = _sitio(sitio)
    productos = sitio.productos.filter(publicado=True)
    categorias = productos.order_by('categoria').values_list('categoria', flat=True).distinct()
    categoria = request.GET.get('categoria')
    if categoria:
        productos = productos.filter(categoria=categoria)
    return render(request, 'nichos/productos.html', {
        'sitio': sitio,
        'productos': productos,
        'categorias': categorias,
        'categoria': categoria,
    })


def producto(request, sitio, slug):
    sitio = _sitio(sitio)
    producto = get_object_or_404(Producto, sitio=sitio, slug=slug, publicado=True)
    return render(request, 'nichos/producto.html', {
        'sitio': sitio,
        'producto': producto,
        'comparativas': producto.comparativas.filter(publicado=True),
        'similares': sitio.productos.filter(publicado=True, categoria=producto.categoria).exclude(pk=producto.pk)[:3],
    })


def buscar(request, sitio):
    sitio = _sitio(sitio)
    q = request.GET.get('q', '').strip()
    resultados = {}
    if q:
        resultados = {
            'articulos': sitio.articulos.filter(publicado=True).filter(
                Q(titulo__icontains=q) | Q(resumen__icontains=q) | Q(contenido__icontains=q)),
            'comparativas': sitio.comparativas.filter(publicado=True).filter(
                Q(titulo__icontains=q) | Q(resumen__icontains=q) | Q(introduccion__icontains=q)),
            'productos': sitio.productos.filter(publicado=True).filter(
                Q(nombre__icontains=q) | Q(marca__icontains=q) | Q(resumen__icontains=q)),
            'tendencias': sitio.tendencias.filter(
                Q(nombre__icontains=q) | Q(descripcion__icontains=q)),
        }
    total = sum(len(r) for r in resultados.values())
    return render(request, 'nichos/buscar.html', {
        'sitio': sitio,
        'q': q,
        'resultados': resultados,
        'total': total,
    })
