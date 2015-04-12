# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150412_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackteam',
            name='email',
            field=models.EmailField(default=b'', help_text=b'Usaremos este email para comunicarnos con ustedes ', unique=True, max_length=30, verbose_name=b'Email de contacto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='name',
            field=models.CharField(unique=True, max_length=40, verbose_name=b'Team Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(max_length=30, unique=True, null=True, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='rut',
            field=models.CharField(max_length=30, unique=True, null=True, verbose_name=b'RUT/Pasaporte', blank=True),
            preserve_default=True,
        ),
    ]
