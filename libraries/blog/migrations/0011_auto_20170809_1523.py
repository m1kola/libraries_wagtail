# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170808_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindex',
            options={'verbose_name': 'News index'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'News article'},
        ),
    ]