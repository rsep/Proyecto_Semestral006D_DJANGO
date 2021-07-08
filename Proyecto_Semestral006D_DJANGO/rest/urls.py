from django.urls import path
from rest.views import lista_obra, detalle_obra


urlpatterns = [
    path('obras', lista_obra,name="lista_obra"),
    path('obras/<id>', detalle_obra,name="detalle_obra")
]