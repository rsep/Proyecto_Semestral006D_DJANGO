# forms.py

from django import forms
from django.db.models.fields.related import ForeignKey
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
    # bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    # expos = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Biografia
        fields = ['bio', 'expos']
        # fields = '__all__'

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        # fields = '__all__'
        fields = ['precio', 'titulo', 'año', 'historia', 'descripcion', 'tecnica', 'imagen_obra']


