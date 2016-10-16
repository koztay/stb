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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product_field', models.CharField(null=True, choices=[('PRODUCT_TITLE', 'title'), ('PRODUCT_DESCRIPTION', 'description'), ('PRODUCT_CATEGORY', 'category'), ('PRODUCT_IMAGE', 'image'), ('PRODUCT_TYPE', 'type'), ('ATTRIBUTE_TYPE', 'attribute_type'), ('ATTRIBUTE_VALUE', 'attribute_value')], blank=True, max_length=20)),
                ('xml_field', models.CharField(null=True, blank=True, max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImportMap',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='fields',
            name='map',
            field=models.ForeignKey(null=True, blank=True, to='importer.ProductImportMap'),
        ),
    ]
