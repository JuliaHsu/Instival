# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-21 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0011_auto_20161221_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.URLField(null=True),
        ),
    ]
