# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170108_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
    ]
