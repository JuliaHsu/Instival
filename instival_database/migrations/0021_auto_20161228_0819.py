# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-28 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0020_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
