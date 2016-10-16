# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161011_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributetype',
            name='product_type',
        ),
    ]
