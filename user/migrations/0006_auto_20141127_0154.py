# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20141127_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='cashflow_id',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
