# Generated by Django 3.2.4 on 2021-06-24 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_artista_biografia_obra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biografia',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='obra',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Artista',
        ),
        migrations.DeleteModel(
            name='Biografia',
        ),
        migrations.DeleteModel(
            name='Obra',
        ),
    ]
