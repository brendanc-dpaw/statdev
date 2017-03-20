# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0022_auto_20170315_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='other_supporting_docs',
        ),
        migrations.RemoveField(
            model_name='application',
            name='document_completion',
        ),
        migrations.AddField(
            model_name='application',
            name='document_completion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_completion', to='applications.Document'),
        ),
        migrations.RemoveField(
            model_name='application',
            name='document_determination',
        ),
        migrations.AddField(
            model_name='application',
            name='document_determination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_determination', to='applications.Document'),
        ),
        migrations.RemoveField(
            model_name='application',
            name='document_draft',
        ),
        migrations.AddField(
            model_name='application',
            name='document_draft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_draft', to='applications.Document'),
        ),
        migrations.RemoveField(
            model_name='application',
            name='document_final',
        ),
        migrations.AddField(
            model_name='application',
            name='document_final',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_final', to='applications.Document'),
        ),
        migrations.RemoveField(
            model_name='application',
            name='river_lease_scan_of_application',
        ),
        migrations.AddField(
            model_name='application',
            name='river_lease_scan_of_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='river_lease_scan_of_application', to='applications.Document'),
        ),
    ]
