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


class Biografia(models.Model):
    id_bio = models.AutoField(primary_key=True, verbose_name='Id Bio')
    bio = models.TextField(max_length=150, verbose_name='Bio')
    expos = models.TextField(max_length=150, verbose_name='Expos')
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_bio)

class Obra(models.Model):
    id_obra = models.AutoField(primary_key=True, verbose_name='Id Obra')
    precio = models.IntegerField(verbose_name='Precio')
    titulo = models.CharField(max_length=50, verbose_name='Título')
    año = models.IntegerField(verbose_name='Año')
    historia = models.TextField(max_length=200, verbose_name='Historia')
    descripcion = models.TextField(max_length=200, verbose_name='Descripcion')
    tecnica = models.CharField(max_length=150, verbose_name='Técnica')
    imagen_obra = models.ImageField(upload_to='uploads/')
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    # def __str__(self):
    #     return str(self.id_obra)

    # para asegurar que al realizar un delete, borre la carga de foto en carpeta uploads de media
    def delete(self, *args, **kwargs):
        self.imagen_obra.delete()
        super().delete(*args, **kwargs)