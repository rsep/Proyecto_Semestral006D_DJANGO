# forms.py

from django import forms
from django.db.models.fields.related import ForeignKey
from django.forms import ModelForm
from django.forms import fields
from .models import Artista, Biografia, Contacto, Obra


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


class ContactoForm(ModelForm):
    class Meta:
        # esta clase (Meta) toma los tipos de datos del modelo que ya está definidio en Models (por eso  se importa)
        model = Contacto
        fields = '__all__'

