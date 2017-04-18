# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parked',
            name='time_slots',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='spots',
            name='radius',
            field=models.CharField(max_length=100),
        ),
    ]
