from django.contrib import admin
from .models import Obra, Artista, Biografia


# Register your models here.
admin.site.register(Obra)
admin.site.register(Artista)
admin.site.register(Biografia)