from django.db.models import fields
from core.models import Obra
from django.db.models.base import Model
from rest_framework import fields, serializers

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'
        # fields = ['id_obra','precio','titulo','año','historia','descripcion','tecnica','imagen_obra','autor']