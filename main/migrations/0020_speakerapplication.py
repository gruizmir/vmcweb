# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20160425_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name=b'Apellido')),
                ('occupation', models.CharField(max_length=200, null=True, verbose_name=b'Cargo/Trabajo', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name=b'Email', blank=True)),
                ('profile_picture', models.ImageField(upload_to=b'speakers', null=True, verbose_name=b'Logo', blank=True)),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Fono', blank=True)),
                ('twitter', models.CharField(max_length=60, null=True, verbose_name=b'Twitter', blank=True)),
                ('linkedin', models.CharField(max_length=200, null=True, verbose_name=b'Linkedin', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'T\xc3\xadtulo de la charla')),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('version', models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creaci\xc3\xb3n')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Actualizaci\xc3\xb3n')),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
    ]
