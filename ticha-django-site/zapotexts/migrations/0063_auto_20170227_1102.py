# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-27 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0062_auto_20170208_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='handwrittentext',
            name='timeline_spanish_headline',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='handwrittentext',
            name='timeline_spanish_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
