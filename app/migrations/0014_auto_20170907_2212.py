# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170907_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
