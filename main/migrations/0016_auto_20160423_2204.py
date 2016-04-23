# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20160423_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AlterModelOptions(
            name='sponsor',
            options={'verbose_name': 'Auspiciador', 'verbose_name_plural': 'Auspiciadores'},
        ),
        migrations.AddField(
            model_name='speaker',
            name='occupation',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Cargo/Trabajo', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='email',
            field=models.EmailField(max_length=100, verbose_name=b'Email'),
        ),
    ]
