from django.db.models import fields
from Proyecto_Semestral006D_DJANGO.core.models import Obra
from django.db.models.base import Model
from rest_framework import serializers
from core.models import Obra
class ObraSerializer(Serializers.ModelSerializers):
    class Meta:
        model: Obra
        fields = ['id_obra','precio','titulo','año','historia','descripcion','tecnica','imagen_obra','autor']
