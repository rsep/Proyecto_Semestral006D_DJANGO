# Generated by Django 3.2.4 on 2021-06-23 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0019_auto_20210623_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Artista')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('password', models.CharField(max_length=5, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id_obra', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Obra')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('año', models.IntegerField(verbose_name='Año')),
                ('historia', models.TextField(max_length=200, verbose_name='Historia')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('tecnica', models.CharField(max_length=150, verbose_name='Técnica')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista')),
            ],
        ),
        migrations.CreateModel(
            name='Biografia',
            fields=[
                ('id_bio', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Bio')),
                ('bio', models.TextField(max_length=150, verbose_name='Bio')),
                ('expos', models.TextField(max_length=150, verbose_name='Expos')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista')),
            ],
        ),
    ]
