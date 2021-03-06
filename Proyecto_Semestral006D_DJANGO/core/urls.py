# archivo URLS del core
# hacer mapeo para abrir el archivo html (entre lo que se escribe en url v/s lo que se va a mostrar)
from collections import namedtuple
from django.urls import path
from .views import index, modificar_obra, nosotros, ficha_obra, galeria_obras, galeria_artistas, perfil, contacto, registro

from .views import bio_artista, listar, eliminar
from .views import test, test2

from .views import test, test2, listar, eliminar, test3

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('ficha_obra/<id>', ficha_obra, name="ficha_obra"),
    path('obras/',galeria_obras, name="galeria_obras"),
    path('artistas/', galeria_artistas, name="galeria_artistas"),
    path('bio/<id>',bio_artista, name="bio_artista"),


    path('perfil/<id>', perfil, name="perfil"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),

    path('test3/<id>', test3, name="test3"),
    
    path('test/', test, name="test"),
    path('test2/',test2, name="test2"),
    path('listar/<id>',listar, name="listar"),
    path('eliminar/<id>',eliminar, name="eliminar"),
    path('obras/editar/<id>',modificar_obra, name="modificar_obra"),
]
