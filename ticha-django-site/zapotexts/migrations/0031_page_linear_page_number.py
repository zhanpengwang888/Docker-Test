# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0030_printed_paginate'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='linear_page_number',
            field=models.IntegerField(null=True),
        ),
    ]
