from django.urls import path
from rest.views import lista_obras, detalle_obra
from .viewslogin import login

urlpatterns = [
    path('obras', lista_obras,name="lista_obra"),
    path('obras/<id>', detalle_obra,name="detalle_obra"),
    path('login', login, name='login'),
]