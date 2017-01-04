# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20170104_1617'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tedarikci',
            new_name='Vendor',
        ),
    ]
