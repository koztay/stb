# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20170222_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]
