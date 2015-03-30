# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=None, verbose_name=b'Nombre', blank=None)),
                ('lastname', models.CharField(max_length=30, null=None, verbose_name=b'Apellido', blank=None)),
                ('rut', models.CharField(max_length=30, null=None, verbose_name=b'RUT/Pasaporte', blank=None)),
                ('email', models.EmailField(max_length=40, null=None, verbose_name=b'Email', blank=None)),
                ('twitter', models.CharField(max_length=30, null=None, verbose_name=b'Twitter', blank=None)),
                ('institution', models.CharField(max_length=30, null=None, verbose_name=b'RUT/Pasaporte', blank=None)),
                ('expositor', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
            bases=(models.Model,),
        ),
    ]
