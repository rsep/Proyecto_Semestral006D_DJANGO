# forms.py

from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Artista

class ArtistaForm(ModelForm):
    class Meta:
        # modelo asociado
        model = Artista
        # fields = ['id_artista', 'nombre', 'email', 'password', 'foto_perfil']
        fields = '__all__'