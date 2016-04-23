# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150903_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name=b'Apellido')),
                ('email', models.EmailField(unique=True, max_length=100, verbose_name=b'Email')),
                ('profile_picture', models.ImageField(upload_to=b'logos', null=True, verbose_name=b'Logo', blank=True)),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Fono', blank=True)),
                ('twitter', models.CharField(max_length=60, null=True, verbose_name=b'Twitter', blank=True)),
                ('linkedin', models.CharField(max_length=200, null=True, verbose_name=b'Linkedin', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Nombre de la app')),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('day', models.IntegerField(null=True, verbose_name=b'D\xc3\xada', blank=True)),
                ('start_time', models.TimeField(null=True, verbose_name=b'Inicio de charla', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creaci\xc3\xb3n')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Actualizaci\xc3\xb3n')),
            ],
        ),
        migrations.AlterField(
            model_name='pitch',
            name='extras',
            field=models.FileField(upload_to=b'pitches', null=True, verbose_name=b'Anexos', blank=True),
        ),
    ]
