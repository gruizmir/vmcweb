# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160423_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackteam',
            name='person5',
        ),
        migrations.RemoveField(
            model_name='hackteam',
            name='person5_code',
        ),
        migrations.AddField(
            model_name='hackteam',
            name='team_picture',
            field=models.ImageField(upload_to=b'hackathon', null=True, verbose_name=b'Foto Equipo', blank=True),
        ),
        migrations.AddField(
            model_name='hackteam',
            name='version',
            field=models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)'),
        ),
        migrations.AddField(
            model_name='pitch',
            name='version',
            field=models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='version',
            field=models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='version',
            field=models.IntegerField(default=2016, verbose_name='Versi\xf3n (A\xf1o)'),
        ),
    ]
