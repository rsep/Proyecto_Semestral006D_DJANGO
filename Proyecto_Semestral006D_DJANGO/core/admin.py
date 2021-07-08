from django.contrib import admin
from .models import Contacto, Obra, Artista, Biografia
# from .models import Artista


# Register your models here.
admin.site.register(Obra)
admin.site.register(Artista)
admin.site.register(Biografia)
admin.site.register(Contacto)
