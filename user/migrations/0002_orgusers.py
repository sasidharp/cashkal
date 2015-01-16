# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orgusers',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('corpid', models.CharField(max_length=20, verbose_name=b'CORP ID')),
                ('user', models.CharField(max_length=75, verbose_name=b'USER')),
                ('pin', models.CharField(max_length=4, verbose_name=b'PIN')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
