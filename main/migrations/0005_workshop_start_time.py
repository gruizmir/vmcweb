# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150408_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='start_time',
            field=models.TimeField(help_text=b'Rellenar s\xc3\xb3lo si es aceptada', null=True, verbose_name=b'Hora de inicio', blank=True),
            preserve_default=True,
        ),
    ]
