# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20141129_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow_actuals',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 12, 3)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='complaint_categ',
            field=models.CharField(max_length=75, verbose_name='SERVICE REQUEST FOR', default='S', choices=[('N', 'New User Registration'), ('G', 'General Query'), ('U', 'Issue with Login'), ('R', 'Issue with Registration'), ('X', 'Forgot Password'), ('Y', 'Issue with transaction'), ('Y', 'Feedback'), ('S', 'Interested')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='complaint_text',
            field=models.TextField(verbose_name='DESCRIPTION'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(null=True, blank=True, max_length=12, verbose_name='CONTACT NO:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mycashflow',
            name='fdate',
            field=models.DateField(verbose_name='DATE', default=datetime.date(2014, 12, 3)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='TypeofOrg',
            field=models.CharField(max_length=1, verbose_name='USER', choices=[('1', 'Individual'), ('2', 'Organization')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='corpid',
            field=models.CharField(max_length=20, verbose_name='CORP ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='currency',
            field=models.CharField(max_length=4, verbose_name='CURRENCY'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='EMAIL'),
            preserve_default=True,
        ),
    ]
