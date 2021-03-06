# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150412_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paperfile',
            name='paper',
        ),
        migrations.DeleteModel(
            name='PaperFile',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='payed',
            new_name='paid',
        ),
        migrations.AddField(
            model_name='paper',
            name='doc',
            field=models.FileField(default=None, upload_to=b'papers', verbose_name=b'Archivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='extras',
            field=models.FileField(upload_to=b'extras', null=True, verbose_name=b'Anexos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(upload_to=b'logos', null=True, verbose_name=b'Logo', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo_thumb',
            field=models.ImageField(upload_to=b'logos', null=True, verbose_name=b'Thumbnail', blank=True),
        ),
    ]
