# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160515_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakerapplication',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name=b'Email'),
        ),
    ]
