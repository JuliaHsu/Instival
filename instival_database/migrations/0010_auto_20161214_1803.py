# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instival_database', '0009_comment_approved_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
    ]
