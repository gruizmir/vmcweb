# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150412_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackteam',
            name='lider_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='person2_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='person3_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro', blank=True),
            preserve_default=True,
        ),
    ]
