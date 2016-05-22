# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20160522_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'T\xc3\xadtulo')),
                ('description', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('image', models.ImageField(upload_to=b'updates', null=True, verbose_name=b'Foto', blank=True)),
                ('image_thumb', models.ImageField(upload_to=b'updates', null=True, verbose_name=b'Thumbnail', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Actualizaci\xf3n',
                'verbose_name_plural': 'Actualizaciones',
            },
        ),
    ]
