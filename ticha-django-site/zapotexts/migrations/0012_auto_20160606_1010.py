# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0011_auto_20160606_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscriptnew',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
