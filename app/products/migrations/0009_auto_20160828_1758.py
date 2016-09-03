# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_show_on_homepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='show_on_menu',
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
    ]
