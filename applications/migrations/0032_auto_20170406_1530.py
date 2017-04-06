# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0031_auto_20170404_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='publish_documents',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='publish_draft_report',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='publish_final_report',
            field=models.DateField(blank=True, null=True),
        ),
    ]