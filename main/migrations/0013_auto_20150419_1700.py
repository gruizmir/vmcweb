# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150419_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(upload_to=b'logos', null=True, verbose_name=b'Logo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo_thumb',
            field=models.ImageField(upload_to=b'logos', null=True, verbose_name=b'Thumbnail', blank=True),
            preserve_default=True,
        ),
    ]
