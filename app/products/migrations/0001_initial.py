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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=120)),
                ('attribute_type', models.ForeignKey(to='products.AttributeType')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('show_on_homepage', models.BooleanField(default=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, to='products.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', tinymce.models.HTMLField(null=True, blank=True, default='<h1>default description</h1>')),
                ('price', models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('show_on_homepage', models.BooleanField(default=True)),
                ('show_on_popular', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='products.Category', blank=True)),
                ('default', models.ForeignKey(blank=True, related_name='default_category', to='products.Category', null=True)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_featured)),
                ('title', models.CharField(null=True, blank=True, max_length=120)),
                ('text', models.CharField(null=True, blank=True, max_length=220)),
                ('text_right', models.BooleanField(default=False)),
                ('text_css_color', models.CharField(null=True, blank=True, max_length=6)),
                ('show_price', models.BooleanField(default=False)),
                ('make_image_background', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=products.models.image_upload_to)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='Projeksiyon Cihazı', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(choices=[('hd', 'HD'), ('sd', 'SD'), ('medium', 'Medium'), ('micro', 'Micro')], default='hd', max_length=20)),
                ('height', models.CharField(null=True, blank=True, max_length=20)),
                ('width', models.CharField(null=True, blank=True, max_length=20)),
                ('media', models.ImageField(height_field='height', width_field='width', null=True, blank=True, upload_to=products.models.thumbnail_location)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)),
                ('sale_price', models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('inventory', models.IntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, to='products.ProductType', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='product',
            field=models.ForeignKey(blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product',
            field=models.ManyToManyField(to='products.Product', blank=True),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='product_type',
            field=models.ForeignKey(to='products.ProductType'),
        ),
    ]
