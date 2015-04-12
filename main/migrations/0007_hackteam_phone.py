# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150412_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackteam',
            name='phone',
            field=models.CharField(default=b'', help_text=b'Usaremos este tel\xc3\xa9fono para comunicarnos con ustedes ', max_length=30, verbose_name=b'Tel\xc3\xa9fono de contacto'),
            preserve_default=True,
        ),
    ]
