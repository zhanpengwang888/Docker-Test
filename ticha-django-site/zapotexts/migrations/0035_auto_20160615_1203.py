# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0034_auto_20160615_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='linear_page_number',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='printed',
            name='convert_to_html',
            field=models.BooleanField(default=True, help_text='This make take several minutes.', verbose_name='Convert to HTML'),
        ),
        migrations.AlterField(
            model_name='printed',
            name='xml_transcript',
            field=models.FileField(upload_to='', verbose_name='XML Transcript'),
        ),
    ]
