# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0023_auto_20170106_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instival_database.User'),
        ),
    ]
