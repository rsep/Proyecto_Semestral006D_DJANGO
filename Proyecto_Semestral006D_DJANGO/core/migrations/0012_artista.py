# Generated by Django 3.2.4 on 2021-06-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0011_delete_artista'),
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
    ]
