from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'core/index.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def ficha_obra(request):
    return render(request,'core/ficha_obra.html')

def bio_artista(request):
    return render(request,'core/bio_artista.html')

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