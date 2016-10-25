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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('product_field', models.CharField(null=True, blank=True, max_length=20)),
                ('xml_field', models.CharField(null=True, blank=True, max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImportMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('root', models.CharField(null=True, blank=True, max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='fields',
            name='map',
            field=models.ForeignKey(blank=True, to='importer.ProductImportMap', null=True),
        ),
    ]
