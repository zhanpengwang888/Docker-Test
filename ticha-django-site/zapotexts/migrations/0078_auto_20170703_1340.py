# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-03 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0077_dictionarypage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionarypage',
            name='letter',
            field=models.CharField(max_length=2),
        ),
    ]
