# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20170224_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='state',
        ),
        migrations.AddField(
            model_name='referral',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]