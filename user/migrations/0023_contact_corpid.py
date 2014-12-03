# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20141204_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='corpid',
            field=models.CharField(max_length=20, default='INDI'),
            preserve_default=True,
        ),
    ]
