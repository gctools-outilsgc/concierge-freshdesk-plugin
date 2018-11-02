# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concierge_freshdesk_plugin', '0003_auto_20180913_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='secret_key',
            field=models.CharField(max_length=250, null=True),
        ),
    ]