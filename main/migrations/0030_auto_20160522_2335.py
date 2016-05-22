# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20160522_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='profile_thumbnail',
            field=models.ImageField(upload_to=b'speakers', null=True, verbose_name=b'Logo', blank=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='profile_thumbnail',
            field=models.ImageField(upload_to=b'workshops', null=True, verbose_name=b'Thumbnail relator', blank=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='profile_picture',
            field=models.ImageField(upload_to=b'workshops', null=True, verbose_name=b'Foto relator', blank=True),
        ),
    ]
