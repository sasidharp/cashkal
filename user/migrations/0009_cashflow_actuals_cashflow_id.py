# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_cashflow_actuals_cashflow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow_actuals',
            name='cashflow_id',
            field=models.IntegerField(max_length=20, default=0),
            preserve_default=True,
        ),
    ]
