# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0003_historicalorganization_historicalpost'),
        ('user_profile', '0002_auto_20180108_1521'),
        ('position', '0004_merge_20180110_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAssignment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('_string_representation', models.TextField(blank=True, help_text='The string representation of this object', null=True)),
                ('status', models.TextField(choices=[('pending', 'pending'), ('assigned', 'assigned'), ('active', 'active'), ('completed', 'completed'), ('curtailed', 'curtailed')], default='pending')),
                ('curtailment_reason', models.TextField(choices=[('medical', 'medical'), ('clearance', 'clearance'), ('service_need', 'service_need'), ('compassionate', 'compassionate'), ('other', 'other')], null=True)),
                ('create_date', models.DateTimeField(blank=True, editable=False, help_text='The date the assignment was created')),
                ('start_date', models.DateTimeField(help_text='The date the assignment started', null=True)),
                ('estimated_end_date', models.DateTimeField(help_text='The estimated end date based upon tour of duty', null=True)),
                ('end_date', models.DateTimeField(help_text='The date this position was completed or curtailed', null=True)),
                ('service_duration', models.IntegerField(help_text='The duration of a completed assignment in months', null=True)),
                ('update_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='position.Position')),
                ('tour_of_duty', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.TourOfDuty')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.UserProfile')),
            ],
            options={
                'verbose_name': 'historical assignment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPosition',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('_string_representation', models.TextField(blank=True, help_text='The string representation of this object', null=True)),
                ('position_number', models.TextField(help_text='The position number', null=True)),
                ('title', models.TextField(help_text='The position title', null=True)),
                ('is_overseas', models.BooleanField(default=False, help_text='Flag designating whether the position is overseas')),
                ('create_date', models.DateTimeField(help_text='The creation date of the position', null=True)),
                ('update_date', models.DateTimeField(help_text='The update date of this position', null=True)),
                ('effective_date', models.DateTimeField(help_text='The effective date of this position', null=True)),
                ('_seq_num', models.TextField(null=True)),
                ('_title_code', models.TextField(null=True)),
                ('_org_code', models.TextField(null=True)),
                ('_bureau_code', models.TextField(null=True)),
                ('_skill_code', models.TextField(null=True)),
                ('_staff_ptrn_skill_code', models.TextField(null=True)),
                ('_pay_plan_code', models.TextField(null=True)),
                ('_status_code', models.TextField(null=True)),
                ('_service_type_code', models.TextField(null=True)),
                ('_grade_code', models.TextField(null=True)),
                ('_post_code', models.TextField(null=True)),
                ('_language_1_code', models.TextField(null=True)),
                ('_language_2_code', models.TextField(null=True)),
                ('_location_code', models.TextField(null=True)),
                ('_language_req_1_code', models.TextField(null=True)),
                ('_language_req_2_code', models.TextField(null=True)),
                ('_language_1_spoken_proficiency_code', models.TextField(null=True)),
                ('_language_1_reading_proficiency_code', models.TextField(null=True)),
                ('_language_2_spoken_proficiency_code', models.TextField(null=True)),
                ('_language_2_reading_proficiency_code', models.TextField(null=True)),
                ('_create_id', models.TextField(null=True)),
                ('_update_id', models.TextField(null=True)),
                ('_jobcode_code', models.TextField(null=True)),
                ('_occ_series_code', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bureau', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.Organization')),
                ('current_assignment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='position.Assignment')),
                ('description', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='position.CapsuleDescription')),
                ('grade', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='position.Grade')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.Organization')),
                ('post', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.Post')),
                ('skill', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='position.Skill')),
                ('tour_of_duty', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.TourOfDuty')),
            ],
            options={
                'verbose_name': 'historical position',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.RemoveField(
            model_name='skillcone',
            name='_name',
        ),
    ]
