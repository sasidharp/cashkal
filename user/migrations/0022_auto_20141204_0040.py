# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20141203_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='corpid',
        ),
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 12, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycashflow',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 12, 4)),
            preserve_default=True,
        ),
    ]
