# Generated by Django 3.0 on 2020-09-11 01:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votos', '0003_auto_20200910_1256'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='voto',
            unique_together={('votante', 'categoria')},
        ),
    ]
