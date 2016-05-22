# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_update_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackteam',
            name='project_description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
