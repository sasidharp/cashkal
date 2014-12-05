# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20141205_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycashflow',
            name='frequency',
            field=models.CharField(max_length=1, choices=[('M', 'Monthly'), ('W', 'Weekly'), ('D', 'Daily'), ('B', 'Bi Weekly'), ('Q', 'Quarterly'), ('H', 'Half Yearly'), ('Y', 'Yearly'), ('S', 'Ad Hoc')], verbose_name='FREQUENCY', default='C'),
            preserve_default=True,
        ),
    ]
