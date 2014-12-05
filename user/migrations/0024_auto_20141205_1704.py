# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_contact_corpid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='fdate',
            field=models.DateField(default=datetime.date(2014, 12, 5), verbose_name='DATE'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='frequency',
            field=models.CharField(default='C', choices=[('M', 'Monthly'), ('W', 'Weekly'), ('D', 'Daily'), ('B', 'Bi Weekly'), ('Q', 'Quarterly'), ('H', 'Half Yearly'), ('Y', 'Yearly'), ('A', 'Ad Hoc')], max_length=1, verbose_name='FREQUENCY'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycashflow',
            name='fdate',
            field=models.DateField(default=datetime.date(2014, 12, 5), verbose_name='DATE'),
            preserve_default=True,
        ),
    ]
