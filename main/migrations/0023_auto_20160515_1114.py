# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20160515_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='contact_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Contacto'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='email',
            field=models.EmailField(max_length=40, null=True, verbose_name=b'Email'),
        ),
    ]
