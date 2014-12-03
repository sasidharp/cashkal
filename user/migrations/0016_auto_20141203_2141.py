# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20141203_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycashflow',
            name='category',
            field=models.ForeignKey(max_length=75, to='user.expense_categories'),
            preserve_default=True,
        ),
    ]
