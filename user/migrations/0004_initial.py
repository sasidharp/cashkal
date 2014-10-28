# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyUser'
        db.create_table('user_myuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True)),
            ('TypeofOrg', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('name1', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('name2', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('name3', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=120, blank=True)),
            ('search1_tag', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('search2_tag', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('corpid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(null=True, max_length=2, blank=True)),
            ('addr1', self.gf('django.db.models.fields.CharField')(null=True, max_length=60, blank=True)),
            ('addr2', self.gf('django.db.models.fields.CharField')(null=True, max_length=60, blank=True)),
            ('fiscal_year', self.gf('django.db.models.fields.CharField')(null=True, max_length=1, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, max_length=30, blank=True)),
            ('pincode', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(null=True, max_length=2, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('landline', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updatestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('user', ['MyUser'])

        # Adding model 'MYCASHFLOW'
        db.create_table('user_mycashflow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, max_length=20)),
            ('parent', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('corpid', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('direction', self.gf('django.db.models.fields.CharField')(default='O', max_length=75)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user.expense_categories'])),
            ('frequency', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('fdate', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 27, 0, 0))),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3)),
            ('recipient', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(null=True, max_length=2, blank=True)),
            ('paymethod', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('telephone', self.gf('django.db.models.fields.CharField')(null=True, max_length=12, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, max_length=75, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(null=True, max_length=12, blank=True)),
            ('notes1', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('notes2', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('notes3', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.CharField')(default='INITIAL', max_length=30)),
            ('changed_on', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 27, 0, 0))),
        ))
        db.send_create_signal('user', ['MYCASHFLOW'])

        # Adding model 'expense_categories'
        db.create_table('user_expense_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, max_length=20)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('corpid', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('user', ['expense_categories'])

        # Adding model 'cashflow_actuals'
        db.create_table('user_cashflow_actuals', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, max_length=20)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('corpid', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cashflow_id', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('direction', self.gf('django.db.models.fields.CharField')(default='O', max_length=75)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user.expense_categories'])),
            ('frequency', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('fdate', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 27, 0, 0))),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3)),
            ('recipient', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(null=True, max_length=10, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(null=True, max_length=2, blank=True)),
            ('paymethod', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('telephone', self.gf('django.db.models.fields.CharField')(null=True, max_length=12, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, max_length=75, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(null=True, max_length=12, blank=True)),
            ('notes1', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('notes2', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('notes3', self.gf('django.db.models.fields.CharField')(null=True, max_length=75, blank=True)),
            ('actualamount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('acurrency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3)),
        ))
        db.send_create_signal('user', ['cashflow_actuals'])


    def backwards(self, orm):
        # Deleting model 'MyUser'
        db.delete_table('user_myuser')

        # Deleting model 'MYCASHFLOW'
        db.delete_table('user_mycashflow')

        # Deleting model 'expense_categories'
        db.delete_table('user_expense_categories')

        # Deleting model 'cashflow_actuals'
        db.delete_table('user_cashflow_actuals')


    models = {
        'user.cashflow_actuals': {
            'Meta': {'object_name': 'cashflow_actuals'},
            'actualamount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'acurrency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'cashflow_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '12', 'blank': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '12', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'})
        },
        'user.expense_categories': {
            'Meta': {'object_name': 'expense_categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'user.mycashflow': {
            'Meta': {'object_name': 'MYCASHFLOW'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'changed_by': ('django.db.models.fields.CharField', [], {'default': "'INITIAL'", 'max_length': '30'}),
            'changed_on': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '12', 'blank': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'parent': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '75', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '12', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'})
        },
        'user.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'TypeofOrg': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'addr1': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '60', 'blank': 'True'}),
            'addr2': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '60', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'name1': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'name2': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'name3': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '120', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pincode': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10', 'blank': 'True'}),
            'search1_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'search2_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '2', 'blank': 'True'}),
            'updatestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['user']