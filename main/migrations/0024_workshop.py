# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20160515_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, null=True, verbose_name=b'T\xc3\xadtulo')),
                ('teacher', models.CharField(max_length=100, null=True, verbose_name=b'Relator')),
                ('profile_picture', models.ImageField(upload_to=b'speakers', null=True, verbose_name=b'Logo', blank=True)),
                ('twitter', models.CharField(max_length=60, null=True, verbose_name=b'Twitter', blank=True)),
                ('linkedin', models.CharField(max_length=200, null=True, verbose_name=b'Linkedin', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('day', models.IntegerField(blank=True, null=True, verbose_name=b'D\xc3\xada', choices=[(1, b'1'), (2, b'2')])),
                ('start_time', models.TimeField(null=True, verbose_name=b'Inicio de charla', blank=True)),
                ('version', models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creaci\xc3\xb3n')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Actualizaci\xc3\xb3n')),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
    ]
