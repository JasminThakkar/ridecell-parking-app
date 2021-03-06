# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_id', models.IntegerField()),
                ('time_slots', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(default='', max_length=100)),
                ('log', models.CharField(default='', max_length=100)),
                ('radius', models.CharField(blank=True, default='', max_length=100)),
                ('occupied', models.BooleanField(default=False)),
            ],
        ),
    ]
