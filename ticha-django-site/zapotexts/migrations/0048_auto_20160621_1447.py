# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0047_auto_20160621_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='czi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='transcription_regular',
            field=models.TextField(verbose_name='Regular                                                            Transcription'),
        ),
    ]
