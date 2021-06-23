# Generated by Django 3.2.4 on 2021-06-23 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_biografia'),
    ]

    operations = [
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
    ]
