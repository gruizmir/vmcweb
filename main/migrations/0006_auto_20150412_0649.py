# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_workshop_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hacker',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='team',
        ),
        migrations.DeleteModel(
            name='Hacker',
        ),
        migrations.AddField(
            model_name='hackteam',
            name='email',
            field=models.EmailField(default=b'', help_text=b'Usaremos este email para comunicarnos con ustedes ', max_length=30, verbose_name=b'Email de contacto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='leader',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Team leader'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='lider_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person2',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Hacker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person2_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person3',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'Hacker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person3_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person4',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Hacker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person4_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person5',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Hacker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hackteam',
            name='person5_code',
            field=models.CharField(help_text=b'\xc2\xbfRegistrado a las charlas? Ingresa tu c\xc3\xb3digo.', max_length=40, null=True, verbose_name=b'C\xc3\xb3digo registro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hackteam',
            name='name',
            field=models.CharField(max_length=40, verbose_name=b'Team Name'),
        ),
    ]
