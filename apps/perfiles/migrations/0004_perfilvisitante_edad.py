# Generated by Django 3.0 on 2020-09-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_remove_perfilvisitante_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilvisitante',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
