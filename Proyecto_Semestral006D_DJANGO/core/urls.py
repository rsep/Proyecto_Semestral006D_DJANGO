# archivo URLS del core
# hacer mapeo para abrir el archivo html (entre lo que se escribe en url v/s lo que se va a mostrar)
from django.urls import path
from .views import index, nosotros, ficha_obra, bio_artista, galeria_obras, galeria_artistas, perfil, contacto, registro

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('ficha_obra/', ficha_obra, name="ficha_obra"),
    path('bio/',bio_artista,name="bio_artista"),
    path('obras/',galeria_obras, name="galeria_obras"),
    path('artistas/', galeria_artistas, name="galeria_artistas"),
    path('perfil/', perfil, name="perfil"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
]
