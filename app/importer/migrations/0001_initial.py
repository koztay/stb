# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('product_field', models.CharField(max_length=20, blank=True, null=True)),
                ('xml_field', models.CharField(max_length=1200, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImportMap',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('root', models.CharField(max_length=120, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='fields',
            name='map',
            field=models.ForeignKey(blank=True, null=True, to='importer.ProductImportMap'),
        ),
    ]
