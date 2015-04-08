# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150402_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('description', models.TextField(verbose_name=b'Descripci\xc3\xb3n')),
                ('url', models.URLField(null=True, blank=True)),
                ('contact_name', models.CharField(max_length=50, verbose_name=b'Contacto')),
                ('email', models.EmailField(unique=True, max_length=40, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Fono', blank=True)),
                ('logo', models.ImageField(upload_to=b'logos', verbose_name=b'Logo')),
                ('logo_thumb', models.ImageField(upload_to=b'logos', verbose_name=b'Thumbnail')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
