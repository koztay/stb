# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HorizontalBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('sub_title', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionThumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(default='lg', max_length=20, choices=[('lg', 'Large'), ('md', 'Medium'), ('micro', 'Micro')])),
                ('height', models.CharField(max_length=20, blank=True, null=True)),
                ('width', models.CharField(max_length=20, blank=True, null=True)),
                ('media', models.ImageField(blank=True, null=True, width_field='width', height_field='height', upload_to=visual_site_elements.models.thumbnail_location)),
                ('promotion', models.ForeignKey(to='visual_site_elements.Promotion')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('sub_title', models.CharField(max_length=80)),
                ('campaign', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=visual_site_elements.models.image_upload_to)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name_of_person', models.CharField(max_length=120)),
                ('comment', models.TextField()),
                ('comment_date', models.DateField()),
                ('image', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
