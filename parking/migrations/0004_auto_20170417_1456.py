# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 21:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20170330_0253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spots',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='spots',
            old_name='log',
            new_name='longitude',
        ),
    ]
