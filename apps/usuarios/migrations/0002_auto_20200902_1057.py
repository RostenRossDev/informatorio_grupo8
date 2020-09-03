# Generated by Django 3.0 on 2020-09-02 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fecha_nacimiento', models.DateField()),
                ('dni', models.IntegerField()),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Paises')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Sexo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
