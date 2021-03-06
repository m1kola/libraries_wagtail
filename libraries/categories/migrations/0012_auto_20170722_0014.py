# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 00:14
from __future__ import unicode_literals

import categories.models
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('categories', '0011_auto_20170721_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='main_image',
            field=models.ForeignKey(blank=True, help_text='Try to ALWAYS provide a main image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='aboutuspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='categories/blocks/subheading.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='categories/blocks/paragraph.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True))))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('name', wagtail.wagtailcore.blocks.CharBlock(blank=True)), ('position', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Position or affiliation'))))), ('snippet', wagtail.wagtailcore.blocks.RichTextBlock(template='categories/blocks/snippet.html')), ('html', categories.models.EmbedHTML(label='Embed code'))), null=True, verbose_name='Page content'),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='categories/blocks/subheading.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='categories/blocks/paragraph.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True))))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('name', wagtail.wagtailcore.blocks.CharBlock(blank=True)), ('position', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Position or affiliation'))))), ('snippet', wagtail.wagtailcore.blocks.RichTextBlock(template='categories/blocks/snippet.html')), ('html', categories.models.EmbedHTML(label='Embed code'))), null=True, verbose_name='Page content'),
        ),
    ]
