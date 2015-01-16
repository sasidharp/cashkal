# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'EMAIL')),
                ('TypeofOrg', models.CharField(max_length=1, verbose_name=b'User', choices=[(b'1', b'Individual'), (b'2', b'Organization')])),
                ('name1', models.CharField(max_length=120, null=True, verbose_name=b'Name', blank=True)),
                ('name2', models.CharField(max_length=120, null=True, verbose_name=b'Name2', blank=True)),
                ('name3', models.CharField(max_length=120, null=True, verbose_name=b'Name3', blank=True)),
                ('first_name', models.CharField(max_length=120, null=True, verbose_name=b'First Name', blank=True)),
                ('last_name', models.CharField(max_length=120, null=True, verbose_name=b'Last Name', blank=True)),
                ('middle_name', models.CharField(max_length=120, null=True, verbose_name=b'Middle Name', blank=True)),
                ('currency', models.CharField(max_length=4, verbose_name=b'Currency')),
                ('corpid', models.CharField(max_length=20, verbose_name=b'CORP ID')),
                ('title', models.CharField(max_length=2, null=True, verbose_name=b'Title', blank=True)),
                ('addr1', models.CharField(max_length=60, null=True, verbose_name=b'Address Line1', blank=True)),
                ('addr2', models.CharField(max_length=60, null=True, verbose_name=b'Address Line2', blank=True)),
                ('fiscal_year', models.CharField(max_length=1, null=True, verbose_name=b'Fiscal', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name=b'City', blank=True)),
                ('pincode', models.CharField(max_length=10, null=True, verbose_name=b'Pincode', blank=True)),
                ('country', models.CharField(max_length=2, null=True, verbose_name=b'Country', blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name=b'Mobile', blank=True)),
                ('landline', models.CharField(max_length=20, null=True, verbose_name=b'Land Phone', blank=True)),
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
                ('corpid', models.CharField(default=b'INDI', max_length=20)),
                ('cashflow_id', models.IntegerField(default=0, max_length=20)),
                ('direction', models.CharField(default=b'O', max_length=75, verbose_name=b'Direction', choices=[(b'I', b'Incoming'), (b'O', b'Expense')])),
                ('categ', models.CharField(max_length=75, verbose_name=b'Expense Type')),
                ('frequency', models.CharField(default=b'C', max_length=1, verbose_name=b'FREQUENCY', choices=[(b'M', b'Monthly'), (b'W', b'Weekly'), (b'D', b'Daily'), (b'B', b'Bi Weekly'), (b'Q', b'Quarterly'), (b'H', b'Half Yearly'), (b'Y', b'Yearly'), (b'S', b'Ad Hoc')])),
                ('fdate', models.DateField(default=datetime.date(2015, 1, 15), verbose_name=b'DATE')),
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
                ('corpid', models.CharField(default=b'INDI', max_length=20)),
                ('email', models.EmailField(max_length=255, verbose_name=b'Email')),
                ('categ', models.CharField(default=b'S', max_length=75, verbose_name=b'Service Request For', choices=[(b'N', b'New User Registration'), (b'G', b'General Query'), (b'U', b'Issue with Login'), (b'R', b'Issue with Registration'), (b'X', b'Forgot Password'), (b'Y', b'Issue with transaction'), (b'Y', b'Feedback'), (b'S', b'Interested')])),
                ('telephone', models.CharField(max_length=12, null=True, verbose_name=b'Contact No:', blank=True)),
                ('complaint_text', models.TextField(verbose_name=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='expense_categories',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=75)),
                ('corpid', models.CharField(default=b'INDI', max_length=20)),
                ('description', models.CharField(max_length=75, verbose_name=b'Description')),
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
                ('corpid', models.CharField(default=b'INDI', max_length=20)),
                ('direction', models.CharField(default=b'O', max_length=75, verbose_name=b'Direction', choices=[(b'I', b'Incoming'), (b'O', b'Expense')])),
                ('categ', models.CharField(max_length=75, verbose_name=b'Expense Type')),
                ('frequency', models.CharField(default=b'C', max_length=1, verbose_name=b'Frequency', choices=[(b'M', b'Monthly'), (b'W', b'Weekly'), (b'D', b'Daily'), (b'B', b'Bi Weekly'), (b'Q', b'Quarterly'), (b'H', b'Half Yearly'), (b'Y', b'Yearly'), (b'S', b'Ad Hoc')])),
                ('fdate', models.DateField(default=datetime.date(2015, 1, 15), verbose_name=b'Date')),
                ('amount', models.DecimalField(verbose_name=b'Amount', max_digits=8, decimal_places=2)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name=b'Currecny', choices=[(b'USD', b'USD'), (b'INR', b'INR')])),
                ('recipient', models.CharField(max_length=75, null=True, verbose_name=b'Payer/Recipient', blank=True)),
                ('name', models.CharField(max_length=75, null=True, verbose_name=b'Name', blank=True)),
                ('street', models.CharField(max_length=75, null=True, verbose_name=b'Street', blank=True)),
                ('city', models.CharField(max_length=75, null=True, verbose_name=b'City', blank=True)),
                ('zipcode', models.CharField(max_length=10, null=True, verbose_name=b'Zipcode', blank=True)),
                ('region', models.CharField(max_length=2, null=True, verbose_name=b'Region', blank=True)),
                ('paymethod', models.CharField(default=b'C', max_length=1, verbose_name=b'Type of Payment', choices=[(b'C', b'CARD'), (b'W', b'WIRE'), (b'B', b'CASH')])),
                ('telephone', models.CharField(max_length=12, null=True, verbose_name=b'TEL:', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('fax', models.CharField(max_length=12, null=True, verbose_name=b'Fax', blank=True)),
                ('notes1', models.CharField(max_length=75, null=True, verbose_name=b'Notes1', blank=True)),
                ('notes2', models.CharField(max_length=75, null=True, verbose_name=b'Notes2', blank=True)),
                ('notes3', models.CharField(max_length=75, null=True, verbose_name=b'Notes3', blank=True)),
                ('converted', models.CharField(max_length=1, null=True, verbose_name=b'CONVERTED', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='orgusers',
            fields=[
                ('id', models.AutoField(max_length=20, serialize=False, auto_created=True, primary_key=True)),
                ('corpid', models.CharField(max_length=20, verbose_name=b'CORP ID')),
                ('user', models.CharField(max_length=75, verbose_name=b'USER')),
                ('pin', models.CharField(max_length=4, verbose_name=b'PIN')),
                ('main', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
