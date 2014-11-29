# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20141127_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow_actuals',
            name='cashflow_id',
        ),
    ]
