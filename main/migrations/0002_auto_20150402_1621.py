# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Equipos')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, null=True, verbose_name=b'T\xc3\xadtulo')),
                ('abstract', models.TextField(verbose_name=b'Resumen')),
                ('accepted', models.BooleanField(default=False, verbose_name=b'Aceptado')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
            ],
            options={
                'verbose_name': 'Paper',
                'verbose_name_plural': 'Papers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaperFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(upload_to=b'papers', verbose_name=b'Archivo')),
                ('extras', models.FileField(upload_to=b'extras', null=True, verbose_name=b'Anexos', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de registro')),
                ('paper', models.ForeignKey(to='main.Paper')),
            ],
            options={
                'verbose_name': 'Archivo adjunto',
                'verbose_name_plural': 'Archivos adjuntos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=30, null=True, verbose_name=b'Apellido')),
                ('rut', models.CharField(max_length=30, null=True, verbose_name=b'RUT/Pasaporte', blank=True)),
                ('email', models.EmailField(unique=True, max_length=40, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Fono', blank=True)),
                ('twitter', models.CharField(max_length=30, null=True, verbose_name=b'Twitter', blank=True)),
                ('institution', models.CharField(max_length=30, null=True, verbose_name=b'RUT/Pasaporte', blank=True)),
                ('expositor', models.BooleanField(default=False, verbose_name=b'Expositor')),
                ('workshop', models.BooleanField(default=False, verbose_name=b'Asiste a taller')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de registro')),
                ('payed', models.BooleanField(default=False, verbose_name=b'Pagado')),
                ('reg_code', models.CharField(max_length=20, verbose_name=b'C\xc3\xb3digo de registro')),
                ('photo', models.ImageField(upload_to=b'profile_pics', verbose_name=b'Foto')),
                ('photo_thumb', models.ImageField(upload_to=b'profile_pics', verbose_name=b'Thumbnail')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Person')),
                ('has_team', models.BooleanField(default=True)),
                ('team', models.ForeignKey(blank=True, to='main.HackTeam', null=True)),
            ],
            options={
                'verbose_name': 'Hacker',
                'verbose_name_plural': 'Hackers',
            },
            bases=('main.person',),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('description', models.TextField(verbose_name=b'Descripci\xc3\xb3n')),
                ('timespan', models.CharField(max_length=10, verbose_name=b'Duraci\xc3\xb3n')),
                ('assistant', models.ManyToManyField(related_name='assistant', to='main.Person')),
                ('expositor', models.ForeignKey(related_name='Expositor', to='main.Person')),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.AddField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(to='main.Person'),
            preserve_default=True,
        ),
    ]
