# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20141203_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow_actuals',
            name='category',
        ),
        migrations.AddField(
            model_name='cashflow_actuals',
            name='categ',
            field=models.CharField(default=1, verbose_name='EXPENSE TYPE', max_length=75),
            preserve_default=False,
        ),
    ]
