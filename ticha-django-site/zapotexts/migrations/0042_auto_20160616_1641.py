# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0041_remove_page_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
