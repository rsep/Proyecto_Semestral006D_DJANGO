# forms.py

from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Artista, Biografia, Obra

class ArtistaForm(ModelForm):
    class Meta:
        # modelo asociado
        model = Artista
        # fields = ['id_artista', 'nombre', 'email', 'password', 'foto_perfil']
        fields = '__all__'

class BiografiaForm(ModelForm):
    class Meta:
        model = Biografia
        fields = '__all__'

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'