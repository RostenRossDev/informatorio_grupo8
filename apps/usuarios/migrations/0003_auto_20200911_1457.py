# Generated by Django 3.0 on 2020-09-11 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200911_1248'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='directo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nacionalidad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='sexo',
        ),
    ]
