# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20141203_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_categories',
            name='corpid',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
