# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synchronizationjob',
            name='talentmap_model',
            field=models.TextField(help_text='The talentmap model as a string; e.g. position.Position', unique=True),
        ),
    ]
