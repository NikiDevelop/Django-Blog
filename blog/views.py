from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    #realizamos un queryset en donde le pasamos la variable que hemos creado 'buscar'
    #filtramos los post los que esten publicados (estado=True)
    #Usamos paginator, en mi caso en múmero que he usado han sido 3 y 
    # después nos saldría un botón de siguiente para ver los siguientes post
    queryset =  request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    paginator = Paginator(posts, 4) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    #Realizamos la busqueda por titulo y descripcion
    #__icontains no tiene encuenta mayúsculas y minúsculas, solo con que coincida el texto le vale
    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) | 
              Q(descripcion__icontains = queryset)
         ).distinct    

    return render(request, 'index.html', {'posts':posts})



def detallePost(request, post_id): 
        post = get_object_or_404(Post,  pk=post_id) 

        return render(request, 'post.html', {'post':post} )




    
#se pasa el mismo nombre que hemos creado en categoría, 
#y así conseguimos todos los posts que su categoría sea Generales
def cine(request):   
       
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria = Categoria.objects.get(nombre__iexact ='Cine')) 
    paginator = Paginator(posts, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset)
        ).distinct


    return render(request, 'generales.html', {'posts':posts})

def programacion(request):
    #__iexact omite mayúsculas y minúsculas
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria = Categoria.objects.get(nombre__iexact ='Programacion'))
    paginator = Paginator(posts, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) | 
              Q(descripcion__icontains = queryset)
         ).distinct


    return render(request, 'programacion.html', {'posts':posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria = Categoria.objects.get(nombre__iexact ='Tutoriales'))

    paginator = Paginator(posts, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) | 
              Q(descripcion__icontains = queryset)
         ).distinct

    return render(request, 'tutoriales.html', {'posts':posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria = Categoria.objects.get(nombre__iexact ='Tecnologia'))
 
    paginator = Paginator(posts, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) | 
              Q(descripcion__icontains = queryset)
         ).distinct


    return render(request, 'tecnologia.html', {'posts':posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria = Categoria.objects.get(nombre__iexact ='Videojuegos'))

    paginator = Paginator(posts, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if queryset:
         posts = Post.objects.filter(
              Q(titulo__icontains = queryset) | 
              Q(descripcion__icontains = queryset)
         ).distinct

    return render(request, 'videojuegos.html', {'posts':posts})


def contacto(request):

    return render(request, 'contacto.html')


def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, "detalle_post.html", {"post": post})


