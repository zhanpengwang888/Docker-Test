# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-11 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0081_delete_czword'),
    ]

    operations = [
        migrations.AddField(
            model_name='printedtext',
            name='zoomable',
            field=models.BooleanField(default=False),
        ),
    ]
