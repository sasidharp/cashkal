# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MYCASHFLOW.changed_on'
        db.delete_column('user_mycashflow', 'changed_on')


    def backwards(self, orm):
        # Adding field 'MYCASHFLOW.changed_on'
        db.add_column('user_mycashflow', 'changed_on',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 27, 0, 0)),
                      keep_default=False)


    models = {
        'user.cashflow_actuals': {
            'Meta': {'object_name': 'cashflow_actuals'},
            'actualamount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'acurrency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'cashflow_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '12'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '12'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
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
            'amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'changed_by': ('django.db.models.fields.CharField', [], {'default': "'START'", 'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3'}),
            'direction': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '75'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '12'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'notes3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'parent': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'recipient': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'region': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '75'}),
            'telephone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '12'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'})
        },
        'user.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'TypeofOrg': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'addr1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '60'}),
            'addr2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '60'}),
            'city': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'mobile': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'name1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'name2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'name3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '120'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pincode': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10'}),
            'search1_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'search2_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'updatestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        }
    }

    complete_apps = ['user']