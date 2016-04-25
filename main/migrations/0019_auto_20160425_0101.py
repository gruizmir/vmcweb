# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20160424_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name=b'Email', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name=b'T\xc3\xadtulo de la charla'),
        ),
    ]
