# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-05 11:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='introduction',
            field=models.TextField(default=datetime.datetime(2017, 6, 5, 11, 38, 40, 708920, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
