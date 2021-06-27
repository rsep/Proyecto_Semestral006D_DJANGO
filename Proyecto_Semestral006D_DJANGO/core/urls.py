# archivo URLS del core
# hacer mapeo para abrir el archivo html (entre lo que se escribe en url v/s lo que se va a mostrar)
from collections import namedtuple
from django.urls import path
from .views import index, nosotros, ficha_obra, galeria_obras, galeria_artistas, perfil, contacto, registro

from .views import bio_artista, test2, listar, eliminar
# from .views import test

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('ficha_obra/<id>', ficha_obra, name="ficha_obra"),
    path('obras/',galeria_obras, name="galeria_obras"),
    path('artistas/', galeria_artistas, name="galeria_artistas"),
    path('perfil/', perfil, name="perfil"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),

    # test (despues se borra)
    path('bio/<id>',bio_artista, name="bio_artista"),
    
    # path('test/<id>', test, name="test"),
    path('test2/',test2, name="test2"),
    path('listar/',listar, name="listar"),
    path('eliminar/<int:id_artista>',eliminar, name="eliminar"),
]
