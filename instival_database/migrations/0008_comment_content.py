# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0007_auto_20161214_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='Comment...'),
            preserve_default=False,
        ),
    ]
