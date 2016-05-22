# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_hackteam_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='update',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='update',
            name='active',
            field=models.BooleanField(default=False, verbose_name=b'Activo'),
        ),
    ]
