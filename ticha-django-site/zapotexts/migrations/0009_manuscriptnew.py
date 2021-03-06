# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapotexts', '0008_manuscript_date_digitized_es'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManuscriptNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('título', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=30)),
                ('idioma', models.CharField(max_length=30)),
                ('document_type', models.CharField(max_length=50)),
                ('tipo_del_documento', models.CharField(max_length=50)),
                ('material_type', models.CharField(max_length=30)),
                ('archive', models.CharField(max_length=100)),
                ('archivo', models.CharField(max_length=100)),
                ('collection', models.CharField(max_length=100)),
                ('colección', models.CharField(max_length=100)),
                ('call_number', models.CharField(max_length=100)),
                ('número_de_etiqueta', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=30)),
                ('páginas', models.CharField(max_length=30)),
                ('date_digitized', models.DateField()),
                ('year', models.CharField(max_length=10)),
                ('town_modern_official', models.CharField(max_length=100)),
                ('pueblo', models.CharField(max_length=100)),
                ('primary_parties', models.CharField(max_length=200)),
                ('personajes_principales', models.CharField(max_length=200)),
                ('slug', models.SlugField(verbose_name='Ticha ID')),
                ('town_short', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('fecha', models.DateField()),
                ('has_translation', models.CharField(max_length=30)),
                ('transcription', models.TextField()),
                ('scribe', models.CharField(max_length=100)),
                ('escribano', models.CharField(max_length=100)),
                ('is_translation', models.CharField(max_length=30)),
                ('witnesses', models.CharField(max_length=300)),
                ('testigos', models.CharField(max_length=300)),
                ('acknowledgements', models.TextField()),
                ('agradecimientos', models.TextField()),
            ],
        ),
    ]
