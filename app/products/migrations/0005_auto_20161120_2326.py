# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20161120_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(choices=[('$', 'AMERİKAN DOLARI'), ('€', 'EURO')], max_length=10, default='$'),
        ),
    ]
