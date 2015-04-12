# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150412_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackteam',
            name='person4',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Hacker', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='person5',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Hacker', blank=True),
            preserve_default=True,
        ),
    ]
