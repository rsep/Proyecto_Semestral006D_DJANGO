from django.db import models

# Create your models here.
class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True, verbose_name='Id Artista')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=5, verbose_name='Contraseña')

    def __str__(self):
        return self.nombre

class Biografia(models.Model):
    bio = models.TextField(max_length=150, verbose_name='Bio')
    expos = models.TextField(max_length=150, verbose_name='Expos')
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Obra(models.Model):
    precio = models.IntegerField(verbose_name='Precio')
    titulo = models.CharField(max_length=50, verbose_name='Título')
    año = models.IntegerField(verbose_name='Año')
    historia = models.TextField(max_length=200, verbose_name='Historia')
    descripcion = models.TextField(max_length=200, verbose_name='Descripcion')
    tecnica = models.CharField(max_length=150, verbose_name='Técnica')
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo