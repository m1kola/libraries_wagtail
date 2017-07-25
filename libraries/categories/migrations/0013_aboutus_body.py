# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0012_auto_20170722_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutuspage',
            options={'verbose_name': 'Simple "About Us" style page'},
        ),
        migrations.AlterModelOptions(
            name='servicepage',
            options={'verbose_name': 'Complex Blog style page'},
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='body',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')),), null=True, verbose_name='Page content'),
        ),
    ]