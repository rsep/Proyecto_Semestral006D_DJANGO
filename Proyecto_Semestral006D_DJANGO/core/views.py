# from core.models import Obra
from core.forms import ArtistaForm
from django.shortcuts import render, redirect
# from .models import Obra
from .models import Artista
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # obras = Obra.objects.all()
    # datos = {
    #     'obras' : obras
    # }
    # return render(request,'core/index.html',datos)
    return render(request,'core/index.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def ficha_obra(request):
    # obra = Obra.objects.all.get(id_obra = id)
    # datos = {
    #     'obra' : obra
    # }
    # return render(request,'core/ficha_obra.html',datos)
    return render(request,'core/ficha_obra.html')

def bio_artista(request):
    return render(request,'core/bio_artista.html')

def galeria_obras(request):
    return render(request,'core/galeria_obras.html')

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

def test(request):

    # # 1. traer el vehiculo, usar metodo get, traer vehiculo cuya patente es igual al id
    # artista = Artista.objects.get(id_artista = id)

    # # 2. construccion formulario
    # datos = {
    #     'form' : artista
    # }

    if request.method == 'GET':
        artistas = Artista.objects.all()
    datos = { 
        'artistas' : artistas
    }
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