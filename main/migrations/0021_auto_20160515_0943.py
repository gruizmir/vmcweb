# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_speakerapplication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speakerapplication',
            options={'verbose_name': 'Postulaci\xf3n de Speaker', 'verbose_name_plural': 'Postulaciones de Speakers'},
        ),
        migrations.AddField(
            model_name='speakerapplication',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name=b'Aprobado'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name=b'Aprobado'),
        ),
    ]
