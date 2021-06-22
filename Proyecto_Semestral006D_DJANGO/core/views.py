from django.shortcuts import render
from .models import Biografia, Obra, Artista

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def ficha_obra(request):
    # crear lista obras para guardar elementos
    obras = Obra.objects.all()
    # # crear diccionario de datos, dentro del objeto datos, voy a guardar las obras
    datos = {
        'obras' : obras
    }
    return render(request,'core/ficha_obra.html',datos)

def bio_artista(request):
    bios = Biografia.objects.all()
    datos = {
        'bios' : bios
    }
    return render(request,'core/bio_artista.html',datos)

def galeria_obras(request):
    return render(request,'core/galeria_obras.html')

def galeria_artistas(request):
    return render(request,'core/galeria_artistas.html')

def perfil(request):
    return render(request,'core/perfil.html')

def contacto(request):
    return render(request,'core/contacto.html')

def registro(request):
    return render(request,'core/registro.html')