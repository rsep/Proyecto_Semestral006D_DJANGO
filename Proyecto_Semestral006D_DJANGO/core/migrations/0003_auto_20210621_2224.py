# Generated by Django 3.2.4 on 2021-06-22 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210621_2220'),
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
