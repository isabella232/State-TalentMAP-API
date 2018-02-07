# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_merge_20180110_1837'),
        ('glossary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossaryentry',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glossaryentry',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='glossaryentry',
            name='last_editing_user',
            field=models.ForeignKey(help_text='The last user to edit this glossary entry', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_glossary', to='user_profile.UserProfile'),
        ),
    ]
