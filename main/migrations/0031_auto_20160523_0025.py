# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20160522_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='profile_thumbnail',
            field=models.ImageField(upload_to=b'speakers/thumbs', null=True, verbose_name=b'Logo', blank=True),
        ),
        migrations.AlterField(
            model_name='speakerapplication',
            name='profile_picture',
            field=models.ImageField(upload_to=b'speakers/applications', null=True, verbose_name=b'Logo', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo_thumb',
            field=models.ImageField(upload_to=b'logos/thumbs', null=True, verbose_name=b'Thumbnail', blank=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='image_thumb',
            field=models.ImageField(upload_to=b'updates/thumbs', null=True, verbose_name=b'Thumbnail', blank=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='profile_picture',
            field=models.ImageField(upload_to=b'workshops/teachers', null=True, verbose_name=b'Foto relator', blank=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='profile_thumbnail',
            field=models.ImageField(upload_to=b'workshops/thumbs', null=True, verbose_name=b'Thumbnail relator', blank=True),
        ),
    ]
