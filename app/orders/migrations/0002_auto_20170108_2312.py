# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='type',
            field=models.CharField(max_length=120, choices=[('billing', 'Fatura Adresi'), ('shipping', 'Sevk Adresi')]),
        ),
    ]
