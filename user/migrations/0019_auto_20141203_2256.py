# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20141203_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflow_actuals',
            name='corpid',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='corpid',
        ),
        migrations.RemoveField(
            model_name='expense_categories',
            name='corpid',
        ),
        migrations.RemoveField(
            model_name='mycashflow',
            name='corpid',
        ),
    ]
