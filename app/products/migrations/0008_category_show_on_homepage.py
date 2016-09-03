# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20160828_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='show_on_homepage',
            field=models.BooleanField(default=True),
        ),
    ]
