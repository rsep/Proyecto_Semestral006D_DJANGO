from django.db import models


# Create your models here.
class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True, verbose_name='Id Artista')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=5, verbose_name='Contraseña')
    foto_perfil = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nombre
    
    # para asegurar que al realizar un delete, borre la carga de foto en carpeta uploads de media
    def delete(self, *args, **kwargs):
        self.foto_perfil.delete()
        super().delete(*args, **kwargs)
