# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MYCASHFLOW.changed_by'
        db.add_column('user_mycashflow', 'changed_by',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True),
                      keep_default=False)

        # Adding field 'MYCASHFLOW.changed_on'
        db.add_column('user_mycashflow', 'changed_on',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 27, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MYCASHFLOW.changed_by'
        db.delete_column('user_mycashflow', 'changed_by')

        # Deleting field 'MYCASHFLOW.changed_on'
        db.delete_column('user_mycashflow', 'changed_on')


    models = {
        'user.cashflow_actuals': {
            'Meta': {'object_name': 'cashflow_actuals'},
            'actualamount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'acurrency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'cashflow_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '12', 'null': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '12', 'null': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'})
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
            'changed_by': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'changed_on': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '12', 'null': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'parent': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '12', 'null': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'})
        },
        'user.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'TypeofOrg': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'addr1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60', 'null': 'True'}),
            'addr2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'name1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'name2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'name3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '120', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pincode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10', 'null': 'True'}),
            'search1_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'search2_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'updatestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        }
    }

    complete_apps = ['user']