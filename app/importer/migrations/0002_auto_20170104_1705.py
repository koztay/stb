# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimportmap',
            name='name',
            field=models.CharField(max_length=120, help_text='Import edeceğimiz dosyaya ilişkin isim'),
        ),
        migrations.AlterField(
            model_name='productimportmap',
            name='root',
            field=models.CharField(null=True, blank=True, max_length=120, help_text="Eğer XML dosyası ise o zaman ürünlerin çekileceği root tagi yaz.\n                                       Buna gerek olmayabilir. Fileds 'dan alınabilir."),
        ),
        migrations.AlterField(
            model_name='productimportmap',
            name='type',
            field=models.CharField(max_length=120, help_text='XML, CSV, XLSX vb.'),
        ),
    ]
