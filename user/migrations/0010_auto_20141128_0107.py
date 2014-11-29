# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_cashflow_actuals_cashflow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycashflow',
            name='converted',
            field=models.CharField(blank=True, verbose_name='CONVERTED', null=True, max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 11, 28)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycashflow',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 11, 28)),
            preserve_default=True,
        ),
    ]
