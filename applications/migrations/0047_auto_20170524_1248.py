# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 04:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0046_auto_20170523_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 24, 12, 48, 4, 32055), verbose_name='Date'),
        ),
    ]