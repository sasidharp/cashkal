# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20141203_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow_actuals',
            name='corpid',
            field=models.CharField(default='INDI', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='corpid',
            field=models.CharField(default='INDI', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expense_categories',
            name='corpid',
            field=models.CharField(default='INDI', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mycashflow',
            name='corpid',
            field=models.CharField(default='INDI', max_length=20),
            preserve_default=True,
        ),
    ]
