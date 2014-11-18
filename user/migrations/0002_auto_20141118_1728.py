# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'Email')),
                ('TypeofOrg', models.CharField(max_length=1, verbose_name=b'Type of Org', choices=[(b'1', b'Individual'), (b'2', b'Organization')])),
                ('name1', models.CharField(max_length=120, null=True, verbose_name=b'NAME', blank=True)),
                ('name2', models.CharField(max_length=120, null=True, verbose_name=b'NAME2', blank=True)),
                ('name3', models.CharField(max_length=120, null=True, verbose_name=b'NAME3', blank=True)),
                ('first_name', models.CharField(max_length=120, null=True, verbose_name=b'FIRST NAME', blank=True)),
                ('last_name', models.CharField(max_length=120, null=True, verbose_name=b'LAST NAME', blank=True)),
                ('middle_name', models.CharField(max_length=120, null=True, verbose_name=b'MIDDLE NAME', blank=True)),
                ('currency', models.CharField(max_length=4, verbose_name=b'Currency')),
                ('corpid', models.CharField(max_length=20, verbose_name=b'Corp.Id')),
                ('calpro', models.CharField(max_length=1, null=True, verbose_name=b'Calendar Profile', blank=True)),
                ('title', models.CharField(max_length=2, null=True, verbose_name=b'TITLE', blank=True)),
                ('addr1', models.CharField(max_length=60, null=True, verbose_name=b'ADDRESS LINE1', blank=True)),
                ('addr2', models.CharField(max_length=60, null=True, verbose_name=b'ADDRESS LINE2', blank=True)),
                ('fiscal_year', models.CharField(max_length=1, null=True, verbose_name=b'FISCAL', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name=b'CITY', blank=True)),
                ('pincode', models.CharField(max_length=10, null=True, verbose_name=b'PINCODE', blank=True)),
                ('country', models.CharField(max_length=2, null=True, verbose_name=b'COUNTRY', blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name=b'MOBILE', blank=True)),
                ('landline', models.CharField(max_length=20, null=True, verbose_name=b'LAND PHONE', blank=True)),
                ('fax', models.CharField(max_length=20, null=True, verbose_name=b'FAX', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updatestamp', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cashflow_actuals',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=75)),
                ('corpid', models.CharField(max_length=5)),
                ('cashflow_id', models.CharField(max_length=5)),
                ('direction', models.CharField(default=b'O', max_length=75, verbose_name=b'DIRECTION', choices=[(b'I', b'Incoming'), (b'O', b'Expense')])),
                ('frequency', models.CharField(default=b'C', max_length=1, verbose_name=b'FREQUENCY', choices=[(b'M', b'Monthly'), (b'W', b'Weekly'), (b'D', b'Daily'), (b'B', b'Bi Weekly'), (b'Q', b'Quarterly'), (b'H', b'Half Yearly'), (b'Y', b'Yearly'), (b'S', b'Custom')])),
                ('fdate', models.DateField(default=datetime.date(2014, 11, 18), verbose_name=b'DATE')),
                ('amount', models.DecimalField(verbose_name=b'AMOUNT', max_digits=8, decimal_places=2)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name=b'CURRENCY', choices=[(b'USD', b'USD'), (b'INR', b'INR')])),
                ('recipient', models.CharField(max_length=75, null=True, verbose_name=b'PAYER/RECIPIENT', blank=True)),
                ('name', models.CharField(max_length=75, null=True, verbose_name=b'NAME', blank=True)),
                ('street', models.CharField(max_length=75, null=True, verbose_name=b'STREET', blank=True)),
                ('city', models.CharField(max_length=75, null=True, verbose_name=b'CITY', blank=True)),
                ('zipcode', models.CharField(max_length=10, null=True, verbose_name=b'ZIPCODE', blank=True)),
                ('region', models.CharField(max_length=2, null=True, verbose_name=b'REGION', blank=True)),
                ('paymethod', models.CharField(default=b'C', max_length=1, verbose_name=b'TYPE OF PAYMENT', choices=[(b'C', b'CARD'), (b'W', b'WIRE'), (b'B', b'CASH')])),
                ('telephone', models.CharField(max_length=12, null=True, verbose_name=b'TEL:', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('fax', models.CharField(max_length=12, null=True, verbose_name=b'FAX', blank=True)),
                ('notes1', models.CharField(max_length=75, null=True, verbose_name=b'NOTES1', blank=True)),
                ('notes2', models.CharField(max_length=75, null=True, verbose_name=b'NOTES2', blank=True)),
                ('notes3', models.CharField(max_length=75, null=True, verbose_name=b'NOTES3', blank=True)),
                ('actualamount', models.DecimalField(verbose_name=b'ACTUAL AMOUNT', max_digits=8, decimal_places=2)),
                ('acurrency', models.CharField(default=b'USD', max_length=3, verbose_name=b'CURRENCY', choices=[(b'USD', b'USD'), (b'INR', b'INR')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=75)),
                ('corpid', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=255, verbose_name=b'Email')),
                ('complaint_categ', models.CharField(default=b'S', max_length=75, verbose_name=b'Category', choices=[(b'N', b'New User Registration'), (b'G', b'General Query'), (b'U', b'Issue with Login'), (b'R', b'Issue with Registration'), (b'X', b'Forgot Password'), (b'Y', b'Issue with transaction'), (b'Y', b'Feedback'), (b'S', b'Interested')])),
                ('telephone', models.CharField(max_length=12, null=True, verbose_name=b'TEL:', blank=True)),
                ('complaint_text', models.CharField(max_length=75, verbose_name=b'DESCRIPTION')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='expense_categories',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=3, verbose_name=b'CATEGORY')),
                ('user', models.CharField(max_length=75)),
                ('corpid', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=75, verbose_name=b'DESCRIPTION')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MYCASHFLOW',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('parent', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=75)),
                ('corpid', models.CharField(max_length=5)),
                ('direction', models.CharField(default=b'O', max_length=75, verbose_name=b'DIRECTION', choices=[(b'I', b'Incoming'), (b'O', b'Expense')])),
                ('frequency', models.CharField(default=b'C', max_length=1, verbose_name=b'FREQUENCY', choices=[(b'M', b'Monthly'), (b'W', b'Weekly'), (b'D', b'Daily'), (b'B', b'Bi Weekly'), (b'Q', b'Quarterly'), (b'H', b'Half Yearly'), (b'Y', b'Yearly'), (b'S', b'Custom')])),
                ('fdate', models.DateField(default=datetime.date(2014, 11, 18), verbose_name=b'DATE')),
                ('amount', models.DecimalField(verbose_name=b'AMOUNT', max_digits=8, decimal_places=2)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name=b'CURRENCY', choices=[(b'USD', b'USD'), (b'INR', b'INR')])),
                ('recipient', models.CharField(max_length=75, null=True, verbose_name=b'PAYER/RECIPIENT', blank=True)),
                ('name', models.CharField(max_length=75, null=True, verbose_name=b'NAME', blank=True)),
                ('street', models.CharField(max_length=75, null=True, verbose_name=b'STREET', blank=True)),
                ('city', models.CharField(max_length=75, null=True, verbose_name=b'CITY', blank=True)),
                ('zipcode', models.CharField(max_length=10, null=True, verbose_name=b'ZIPCODE', blank=True)),
                ('region', models.CharField(max_length=2, null=True, verbose_name=b'REGION', blank=True)),
                ('paymethod', models.CharField(default=b'C', max_length=1, verbose_name=b'TYPE OF PAYMENT', choices=[(b'C', b'CARD'), (b'W', b'WIRE'), (b'B', b'CASH')])),
                ('telephone', models.CharField(max_length=12, null=True, verbose_name=b'TEL:', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('fax', models.CharField(max_length=12, null=True, verbose_name=b'FAX', blank=True)),
                ('notes1', models.CharField(max_length=75, null=True, verbose_name=b'NOTES1', blank=True)),
                ('notes2', models.CharField(max_length=75, null=True, verbose_name=b'NOTES2', blank=True)),
                ('notes3', models.CharField(max_length=75, null=True, verbose_name=b'NOTES3', blank=True)),
                ('category', models.ForeignKey(verbose_name=b'EXPENSE TYPE', to='user.expense_categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cashflow_actuals',
            name='category',
            field=models.ForeignKey(verbose_name=b'EXPENSE TYPE', to='user.expense_categories'),
            preserve_default=True,
        ),
    ]
