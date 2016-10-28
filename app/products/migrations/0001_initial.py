# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models
import taggit.managers
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(default='', max_length=120)),
                ('attribute_type', models.ForeignKey(to='products.AttributeType')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('show_on_homepage', models.BooleanField(default=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', tinymce.models.HTMLField(default='<h1>default description</h1>', blank=True, null=True)),
                ('price', models.DecimalField(blank=True, max_digits=20, null=True, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('show_on_homepage', models.BooleanField(default=True)),
                ('show_on_popular', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(blank=True, to='products.Category')),
                ('default', models.ForeignKey(related_name='default_category', blank=True, null=True, to='products.Category')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_featured)),
                ('title', models.CharField(max_length=120, blank=True, null=True)),
                ('text', models.CharField(max_length=220, blank=True, null=True)),
                ('text_right', models.BooleanField(default=False)),
                ('text_css_color', models.CharField(max_length=6, blank=True, null=True)),
                ('show_price', models.BooleanField(default=False)),
                ('make_image_background', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(default='Projeksiyon Cihazı', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(default='hd', max_length=20, choices=[('hd', 'HD'), ('sd', 'SD'), ('medium', 'Medium'), ('micro', 'Micro')])),
                ('height', models.CharField(max_length=20, blank=True, null=True)),
                ('width', models.CharField(max_length=20, blank=True, null=True)),
                ('media', models.ImageField(blank=True, null=True, width_field='width', height_field='height', upload_to=products.models.thumbnail_location)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(blank=True, max_digits=20, null=True, decimal_places=2)),
                ('sale_price', models.DecimalField(blank=True, max_digits=20, null=True, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('inventory', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, to='products.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='product',
            field=models.ForeignKey(blank=True, null=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product_type',
            field=models.ForeignKey(to='products.ProductType'),
        ),
    ]
