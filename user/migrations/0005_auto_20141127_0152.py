# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20141127_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='cashflow_id',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
