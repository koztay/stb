# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import products.utils


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0009_auto_20160528_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('micro', 'Micro')], default='hd',
                                          max_length=20)),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('width', models.CharField(max_length=20, null=True, blank=True)),
                ('media', models.ImageField(blank=True, width_field='width', height_field='height', null=True,
                                            upload_to=products.utils.thumbnail_location)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
