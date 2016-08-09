# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0008_productfeatured_text_css_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('order', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=120)),
                ('product', models.ManyToManyField(to='products.Product', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.CharField(max_length=120, default='')),
                ('attribute_type', models.ForeignKey(to='products.AttributeType')),
                ('product', models.ForeignKey(null=True, blank=True, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=120, default='Projeksiyon Cihazı')),
            ],
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product_type',
            field=models.ForeignKey(to='products.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductType'),
        ),
    ]
