# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='day_one',
            field=models.BooleanField(default=False, help_text=b'Participa en el d\xc3\xada 1. Si est\xc3\xa1 desmarcado, participa en d\xc3\xada 2', verbose_name=b'\xc2\xbfD\xc3\xada 1?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paper',
            name='start_time',
            field=models.TimeField(help_text=b'Rellenar s\xc3\xb3lo si es aceptada', null=True, verbose_name=b'Hora de inicio', blank=True),
            preserve_default=True,
        ),
    ]
