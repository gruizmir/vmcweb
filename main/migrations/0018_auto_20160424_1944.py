# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20160424_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='contact_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Contacto', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='email',
            field=models.EmailField(max_length=40, null=True, verbose_name=b'Email', blank=True),
        ),
    ]
