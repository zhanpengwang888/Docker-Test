# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-25 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0056_handwrittentext_interlinear_analysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printedtext',
            name='xml_transcript',
            field=models.FileField(blank=True, upload_to='', verbose_name='XML Transcript'),
        ),
    ]
