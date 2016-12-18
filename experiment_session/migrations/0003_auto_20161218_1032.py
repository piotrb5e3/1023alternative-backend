# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 10:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment_session', '0002_auto_20161201_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='combination',
            name='status',
            field=models.CharField(choices=[('F', 'Finished'), ('P', 'In progress')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='experimentsession',
            name='number',
            field=models.IntegerField(default=1, validators=(django.core.validators.MinValueValidator(1),)),
            preserve_default=False,
        ),
    ]