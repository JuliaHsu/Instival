# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-22 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0012_auto_20161216_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
            ],
        ),
    ]
