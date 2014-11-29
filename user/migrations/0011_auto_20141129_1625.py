# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20141128_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense_categories',
            name='category',
        ),
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 11, 29)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycashflow',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 11, 29)),
            preserve_default=True,
        ),
    ]
