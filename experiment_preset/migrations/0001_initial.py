# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 16:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('timeout_mode', models.CharField(choices=[('fixed', 'Fixed'), ('responsive', 'Responsive')], max_length=30)),
                ('timeout_value', models.IntegerField(validators=(django.core.validators.MinValueValidator(0),))),
                ('feedback_mode', models.CharField(choices=[('none', 'None'), ('n_audio', 'Audio on error')], max_length=30)),
                ('repeats_count', models.IntegerField(validators=(django.core.validators.MinValueValidator(0),))),
            ],
        ),
    ]