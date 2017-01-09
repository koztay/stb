# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_product_default'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='buying_curreny',
            new_name='buying_currency',
        ),
    ]
