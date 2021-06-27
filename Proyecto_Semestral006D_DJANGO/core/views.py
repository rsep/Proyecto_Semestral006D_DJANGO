# from core.models import Obra
from core.forms import ArtistaForm, ObraForm, BiografiaForm
from django.shortcuts import render, redirect
from .models import Artista, Obra, Biografia
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
# OK
def index(request):
    if request.method == 'GET':
        artistas = Artista.objects.all()
        # obras = Obra.objects.all()
        # obra = Obra.objects.filter(autor = 3)
    datos = { 
        'artistas' : artistas
        # 'obra' : obra
    }
    return render(request,'core/index.html',datos)

# OK
def nosotros(request):
    return render(request,'core/nosotros.html')

# OK
def ficha_obra(request,id):
    obra = get_object_or_404(Obra, id_obra = id)
    # identificador = Obra.autor
    # artista = get_object_or_404(Artista, id_artista = identificador)

    # 2. construccion formulario
    datos = {
        # 'artista' : artista,
        'obra' : obra
    }
    return render(request, 'core/ficha_obra.html', datos)

# OK
def galeria_obras(request):
    if request.method == 'GET':
        obras = Obra.objects.all()
    datos = { 
        'obras' : obras
    }
    return render(request,'core/galeria_obras.html',datos)

# OK
def galeria_artistas(request):
    if request.method == 'GET':
        artistas = Artista.objects.all()
    datos = { 
        'artistas' : artistas
    }
    return render(request,'core/galeria_artistas.html',datos)

def perfil(request):
    return render(request,'core/perfil.html')

def contacto(request):
    return render(request,'core/contacto.html')

def registro(request):
    return render(request,'core/registro.html')

# OK
def bio_artista(request,id):
# ejemplo de bio_artista (instancias de Artista, Biografia, Obra)
    # 1. traer el vehiculo, usar metodo get, traer vehiculo cuya patente es igual al id
    artista = get_object_or_404(Artista, id_artista = id)
    bio = get_object_or_404(Biografia, autor = id)

    # 2. construccion formulario
    datos = {
        'artista' : artista,
        'bio' : bio
    }   
    
    return render(request,'core/bio_artista.html',datos)



# -----------------------------------------------------
# TESTEOS
# -----------------------------------------------------

def test(request,id):
        # 1. traer el vehiculo, usar metodo get, traer vehiculo cuya patente es igual al id
    bio = Biografia.objects.get(id_bio = id)

    # 2. construccion formulario
    datos = {
        # doc : bio.bio,
        'form' : BiografiaForm(instance=id)
    }

    if request.method == 'POST':
        formulario = BiografiaForm(data=request.POST, instance=id)
        # verificar que el formulario sea valido
        if formulario.is_valid:
            # debo guardar el formulario
            formulario.save()
            # mensaje de texto
            datos['mensaje']='Datos modificados exitosamente'
        
    return render(request,'core/test.html',datos)


def test2(request):
    datos = {
    'form' : ArtistaForm()
    # va a ser una nueva instancia
    }

    if request.method == 'POST':
        formulario = ArtistaForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Artista agregado exitosamente'
        else:
            datos['form'] = formulario

    return render(request,'core/test2.html',datos)


def listar(request):
    # 1. crear lista vehiculos para guardar elementos
    artistas = Artista.objects.all()

    # 2. crear diccionario de datos, dentro del objeto datos, voy a guardar los vehiculos
    datos = {
        'artistas' : artistas
    }
    return render(request,'core/listar.html',datos)

def eliminar(request,id):
    artista = Artista.objects.get(id_artista=id)
    artista.delete()
    # hacer un redirect que es cambiar de vista
    return redirect(to='listar')