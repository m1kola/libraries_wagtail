# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='e.g. Meyer Fall 2017', max_length=200)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('mon', models.CharField(max_length=150)),
                ('tues', models.CharField(max_length=150)),
                ('wednes', models.CharField(max_length=150)),
                ('thurs', models.CharField(max_length=150)),
                ('fri', models.CharField(max_length=150)),
                ('satur', models.CharField(max_length=150)),
                ('sun', models.CharField(max_length=150)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='hours.Library')),
            ],
        ),
    ]