# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0022_auto_20170106_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='instival_database.User'),
        ),
    ]
