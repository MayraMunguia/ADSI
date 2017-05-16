# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hope', '0002_auto_20170512_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='created_date',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='Correo',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='Nombre',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='Asunto',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='Mensaje',
            field=models.TextField(null=True),
        ),
    ]
