# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20141203_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycashflow',
            name='category',
            field=models.CharField(verbose_name='EXPENSE TYPE', max_length=75),
            preserve_default=True,
        ),
    ]
