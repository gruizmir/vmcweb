# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150425_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name=b'Apellido')),
                ('email', models.EmailField(unique=True, max_length=100, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name=b'Fono', blank=True)),
                ('app_name', models.CharField(max_length=100, null=True, verbose_name=b'Nombre de la app')),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('accepted', models.BooleanField(default=False, verbose_name=b'Aceptado')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de registro')),
                ('extras', models.FileField(upload_to=b'extras', null=True, verbose_name=b'Anexos', blank=True)),
            ],
            options={
                'verbose_name': 'Pitch',
                'verbose_name_plural': 'Pitches',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='paper',
            name='authors',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='assistant',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='expositor',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Workshop',
        ),
    ]
