# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20141203_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='complaint_categ',
            new_name='categ',
        ),
    ]
