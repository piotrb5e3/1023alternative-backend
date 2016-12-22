# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 17:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('lightoffmode', models.CharField(choices=[('fixed', 'Fixed'), ('waiting', 'Waiting')], max_length=30)),
                ('lightofftimeout', models.IntegerField(validators=(django.core.validators.MinValueValidator(0),))),
                ('audiomode', models.CharField(choices=[('none', 'None'), ('beep', 'Audible beep on error')], max_length=30)),
                ('repeatscount', models.IntegerField(validators=(django.core.validators.MinValueValidator(1),))),
                ('createdon', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
