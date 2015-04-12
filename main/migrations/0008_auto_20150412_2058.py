# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_hackteam_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackteam',
            name='person4_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='person5_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro', blank=True),
            preserve_default=True,
        ),
    ]
