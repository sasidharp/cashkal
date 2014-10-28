# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MYCASHFLOW.changed_by'
        db.alter_column('user_mycashflow', 'changed_by', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'MYCASHFLOW.changed_by'
        db.alter_column('user_mycashflow', 'changed_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    models = {
        'user.cashflow_actuals': {
            'Meta': {'object_name': 'cashflow_actuals'},
            'actualamount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'acurrency': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'USD'"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'cashflow_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'USD'"}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '75', 'default': "'O'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'C'"}),
            'id': ('django.db.models.fields.AutoField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'C'"}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'user.expense_categories': {
            'Meta': {'object_name': 'expense_categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'max_length': '20', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'user.mycashflow': {
            'Meta': {'object_name': 'MYCASHFLOW'},
            'amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user.expense_categories']"}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'INITIAL'"}),
            'changed_on': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'USD'"}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '75', 'default': "'O'"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'fdate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 27, 0, 0)'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'C'"}),
            'id': ('django.db.models.fields.AutoField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes1': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes2': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes3': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'paymethod': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'C'"}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'user.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'TypeofOrg': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'addr1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'addr2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'corpid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name1': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name2': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name3': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pincode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'search1_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'search2_tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'updatestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['user']