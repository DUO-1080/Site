# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20170130_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artical',
            options={'ordering': ['-create_time']},
        ),
        migrations.RenameField(
            model_name='artical',
            old_name='creat_time',
            new_name='create_time',
        ),
    ]
