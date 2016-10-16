# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevalue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, blank=True, to='products.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='show_on_homepage',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='attribute_types',
            field=models.ManyToManyField(related_name='product_attributes', to='products.AttributeType', through='products.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='attribute_values',
            field=models.ManyToManyField(related_name='product_attr_values', to='products.AttributeValue', through='products.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='show_on_homepage',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='show_on_popular',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='attribute_type',
            field=models.ForeignKey(null=True, blank=True, to='products.AttributeType'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='attribute_value',
            field=models.ForeignKey(null=True, blank=True, to='products.AttributeValue'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='product',
            field=models.ForeignKey(null=True, blank=True, to='products.Product'),
        ),
        migrations.RemoveField(
            model_name='attributetype',
            name='product',
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product',
            field=models.ForeignKey(null=True, blank=True, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(null=True, blank=True, default='<h1>default description</h1>'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='type',
            field=models.CharField(max_length=20, choices=[('hd', 'HD'), ('sd', 'SD'), ('medium', 'Medium'), ('micro', 'Micro')], default='hd'),
        ),
    ]
