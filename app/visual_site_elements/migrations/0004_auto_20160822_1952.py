# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visual_site_elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('visual_site_elements', '0003_promotions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionThumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('lg', 'Large'), ('md', 'Medium'), ('micro', 'Micro')], default='hd', max_length=20)),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('width', models.CharField(max_length=20, null=True, blank=True)),
                ('media', models.ImageField(width_field='width', height_field='height', upload_to=visual_site_elements.models.thumbnail_location, null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Promotions',
            new_name='Promotion',
        ),
        migrations.AddField(
            model_name='promotionthumbnail',
            name='promotion',
            field=models.ForeignKey(to='visual_site_elements.Promotion'),
        ),
    ]
