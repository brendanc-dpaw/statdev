# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0040_auto_20170522_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='document_pre_draft',
        ),
        migrations.AddField(
            model_name='application',
            name='document_new_draft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_newdraft', to='applications.Document'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 15, 52, 34, 969981), verbose_name='Date'),
        ),
    ]