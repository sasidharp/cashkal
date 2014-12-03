# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20141203_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mycashflow',
            old_name='category',
            new_name='categ',
        ),
    ]
