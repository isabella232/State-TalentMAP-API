# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0010_auto_20180212_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalposition',
            name='status',
            field=models.CharField(help_text='Cycle status text', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='historicalposition',
            name='status_code',
            field=models.CharField(help_text='Cycle status code', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='status',
            field=models.CharField(help_text='Cycle status text', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='status_code',
            field=models.CharField(help_text='Cycle status code', max_length=120, null=True),
        ),
    ]
