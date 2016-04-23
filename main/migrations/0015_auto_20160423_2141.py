# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20160423_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='version',
            field=models.IntegerField(default=2016, verbose_name=b'D\xc3\xada'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='day',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'D\xc3\xada', choices=[(1, b'1'), (2, b'2')]),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='profile_picture',
            field=models.ImageField(upload_to=b'speakers', null=True, verbose_name=b'Logo', blank=True),
        ),
    ]
