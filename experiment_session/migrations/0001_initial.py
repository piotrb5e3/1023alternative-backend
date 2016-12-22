# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 17:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Finished'), ('P', 'In progress')], default='P', max_length=1)),
                ('lightset', models.IntegerField(validators=(django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1023)))),
                ('user', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Finished'), ('P', 'In progress')], default='P', max_length=1)),
                ('startedon', models.DateTimeField(auto_now_add=True)),
                ('finishedon', models.DateTimeField(blank=True, null=True)),
                ('userid', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(blank=True, max_length=265, null=True)),
                ('userage', models.IntegerField(blank=True, null=True, validators=(django.core.validators.MinValueValidator(1),))),
                ('usersex', models.CharField(blank=True, choices=[('M', 'Female'), ('F', 'Male')], max_length=1, null=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='experiment.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Repeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Finished'), ('P', 'In progress')], default='P', max_length=1)),
                ('startedon', models.DateTimeField(auto_now_add=True)),
                ('finishedon', models.DateTimeField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repeats', to='experiment_session.ExperimentSession')),
            ],
        ),
        migrations.AddField(
            model_name='combination',
            name='repeat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combinations', to='experiment_session.Repeat'),
        ),
        migrations.AlterUniqueTogether(
            name='repeat',
            unique_together=set([('session', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='combination',
            unique_together=set([('repeat', 'lightset')]),
        ),
    ]
