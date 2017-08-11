# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 06:08
from __future__ import unicode_literals

import categories.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_protect_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('subheading', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='categories/blocks/subheading.html')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='categories/blocks/paragraph.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('position', wagtail.wagtailcore.blocks.CharBlock(label='Position or affiliation', required=False))))), ('snippet', wagtail.wagtailcore.blocks.RichTextBlock(label='Callout', template='categories/blocks/snippet.html')), ('html', categories.models.EmbedHTML(label='Embed code')), ('row', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='categories/blocks/paragraph.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False))))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('name', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('position', wagtail.wagtailcore.blocks.CharBlock(label='Position or affiliation', required=False))))), ('snippet', wagtail.wagtailcore.blocks.RichTextBlock(label='Callout', template='categories/blocks/snippet.html')))))), null=True, verbose_name='Page content'),
        ),
    ]