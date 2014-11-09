from crispy_forms.templatetags.crispy_forms_field import css_class
from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field ,Row,Submit , Button ,Reset
from crispy_forms.bootstrap import StrictButton, PrependedAppendedText , FormActions , StrictButton , UneditableField,\
    AppendedText , FieldWithButtons
from crispy_forms.layout import Div 
from crispy_forms.bootstrap import Tab , TabHolder
from crispy_forms.bootstrap import AppendedText,AppendedPrependedText,InlineField
from .models import MyUser, MYCASHFLOW, expense_categories,cashflow_actuals,MyUser,contact
from django.forms.formsets import formset_factory
import datetime
from django.forms.widgets import Widget
from django.contrib.auth import get_user, get_user_model


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyUser


# class MyOrgUser(MyUser):
#     pass1=models.CharField(max_length=120,null=True,blank=True,verbose_name='password1')
#     pass2=models.CharField(max_length=120,null=True,blank=True,verbose_name='password2')


class NewUser(forms.ModelForm):
    class Meta:
        model = MyUser
    

class NewUserReg(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    
    class Meta:
        model = MyUser
    
    def __init__(self, *args, **kwargs):
        super(NewUserReg, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'USER'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.form_class='form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
              
        self.helper.layout = Layout(
                                        TabHolder(
                                                Tab('BASIC',
                                                     Field('email',autofocus=True),
                                                     Field('password1',placeholder='password1',required=True),
                                                     Field('password2',placeholder='password2',required=True),
                                                     FieldWithButtons('TypeofOrg'),
                                                     Field('name1',placeholder='name1',required=True,css_class='form-horizontal'),
                                                     Field('name2',placeholder='name2',required=True),
                                                     # Field('name3',placeholder='name3',required=True),
                                                     Field('first_name',placeholder='first name',required=True),
                                                     Field('last_name',placeholder='last_name',required=True),
                                                     # Field('middle_name',placeholder='middle_name',required=True),
                                                     Field('currency',placeholder='USD',required=True), 
                                                     Field('corpid',placeholder='corp id',required=True), 
                                                     # Field('title',placeholder='Mr',required=True),
                                                     # Field('fiscal_year',placeholder='year',required=True),
                                                     # Field('city',placeholder='city',required=True),
                                                     # Field('pincode',placeholder='pincode',required=True),
                                                     # Field('country',placeholder='country',required=True),
                                                     Field('mobile',placeholder='mobile',required=True),
                                                     # Field('landline',placeholder='landline',required=True),
                                                     # Field('fax',placeholder='fax',required=True),
                                                     Submit( name='SAVE', value='SAVE',type='Submit',css_class='btn btn-success'),
                                                     Reset( name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')
                                                
                                                )
                                 )
)     

class NewCashForm(forms.ModelForm):
    class Meta:
        model = MYCASHFLOW
   
    def __init__(self, *args, **kwargs):
        super(NewCashForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'cashentry'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
    
        user_curr='NONE'
        if 'initial' in kwargs:
            user_curr = self.initial['currency']
            
        self.helper.layout = Layout(
                TabHolder(
                   Tab( 'DATA ENTRY',
                         Field('direction',autofocus=True),
                         FieldWithButtons('category', StrictButton("Add New!",id='addcateg')),
                         Div(Div('frequency',css_class='col-md-6'),Div('fdate',css_class='col-md-6'),css_class='row'),
#                          InlineField('frequency','fdate'),
# #                         'frequency',
#                         'fdate',
                         AppendedText('amount',user_curr,placeholder='Planned amount',required=True,min="0",max="10000", step="1"),
#                        Field('currency',placeholder='USD',required=True),
                         Field('recipient',placeholder='Payment Recipient / debtor',required=True),
                        'paymethod',
                         Submit( name='SAVE', value='SAVE',type='Submit',css_class='btn btn-success'),
                         Reset( name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')),
                   Tab('ADDRESS',
                       'street',
                       'city',
                       'zipcode',
                       'region'),
                   Tab('CONTACT INFO',
                        Field('telephone'), 
                        'fax',
                        Field('email',placeholder='somebody@gmail.com'), 
                     ),
                   Tab('NOTES',
                        Field('notes1',placeholder='Reminder1'),
                        Field('notes2',placeholder='Collect in cash etc'),
                        Field('notes3',placeholder='Any other information'))
                   )
                )

class NewActualForm(forms.ModelForm):
    class Meta:
        model = cashflow_actuals
        exclude = ['id']
    
    def __init__(self, *args, **kwargs):
        super(NewActualForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'cashentry'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
        
        self.helper.layout = Layout(
                TabHolder(
                   Tab( 'DATA ENTRY',
#                          Field('direction',autofocus=True),
                         FieldWithButtons('category', StrictButton("Add New!",id='addcateg')),
                        'fdate',
                         Field('amount',placeholder='0.99',required=True),
                         Field('currency',placeholder='USD',required=True),
                         Field('recipient',placeholder='Payment Recipient / debtor',required=True),
                        'paymethod',
                         Submit( name='SAVE', value='SAVE',type='Submit',css_class='btn btn-success'),
                         Reset( name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')),
                   Tab('ADDRESS',
                       'street',
                       'city',
                       'zipcode',
                       'region'),
                   Tab('CONTACT INFO',
                       'telephone', 
                        'fax',
                        Field('email',placeholder='somebody@gmail.com'), 
                     ),
                   Tab('NOTES',
                        Field('notes1',placeholder='Reminder1'),
                        Field('notes2',placeholder='Collect in cash etc'),
                        Field('notes3',placeholder='Any other information'))
                   )
                )

class ActualForm(forms.ModelForm):
 
    class Meta:
        model = cashflow_actuals
    
    def __init__(self, *args, **kwargs):
        super(ActualForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'cashentry'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
    
#       get the yser details
        user_curr='NONE'
        if 'initial' in kwargs:
            user_curr = self.initial['currency']
                
        self.helper.layout = Layout(
                TabHolder(
                   Tab( 'DATA ENTRY',
                          Field('direction',autofocus=True),
                          Div(Div('category',css_class='col-md-6'),Div('fdate',css_class='col-md-6'),css_class='row'),
                          AppendedText('actualamount',user_curr,placeholder='Actual amount',required=True,min="0",max="10000", step="1"),
                          Field('recipient',placeholder='Payment Recipient / debtor',required=True),
                         'paymethod',
                          Submit( name='SAVE', value='SAVE',type='Submit',css_class='btn btn-success'),
                          Reset( name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')),
                   Tab('ADDRESS',
                       'street',
                       'city',
                       'zipcode',
                       'region'),
                   Tab('CONTACT INFO',
                       'telephone', 
                        'fax',
                        Field('email',placeholder='somebody@gmail.com'), 
                     ),
                   Tab('NOTES',
                        Field('notes1',placeholder='Reminder1'),
                        Field('notes2',placeholder='Collect in cash etc'),
                        Field('notes3',placeholder='Any other information'))
                   )
                )
          
class NewExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = expense_categories

    def __init__(self, *args, **kwargs):
        super(NewExpenseCategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'expense'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
        
        self.helper.layout = Layout(
                         Row(Field('category',autofocus=True),'description'),
                         Submit(name='SAVE', value='SAVE',type='Submit',css_class='btn btn-success'),
                         Reset(name='RESET', value='RESET',type='Submit',css_class='btn btn-danger'))
  
class ReportSelection(forms.Form):

    category_id=forms.ModelChoiceField(expense_categories.items.all())
    start_date = forms.DateField()
    end_date = forms.DateField()
    
    def __init__(self, *args, **kwargs):
        
        super(ReportSelection, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'report'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
    
        self.helper.layout = Layout(Field('category_id',autofocus=True),
                                    Field('start_date', required=True),
                                    Field('end_date', required=True),
                                    Submit(name='SAVE', value='GET',type='Submit',css_class='btn btn-success'),
                                    Reset(name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')
                               
    )    
    
class PieSelection(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    
    def __init__(self, *args, **kwargs):
        
        super(PieSelection, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'report'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
    
        self.helper.layout = Layout(Field('start_date', value=datetime.date.today()),
                                    Field('end_date', value=datetime.date.today()),
                                    Submit(name='SAVE', value='GET',type='Submit',css_class='btn btn-success'),
                                    Reset(name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')
                               
    )    

class NewContactForm(forms.ModelForm):
    class Meta:
        model = contact
        exclude=['id, user, corpid']

    def __init__(self, *args, **kwargs):

        super(NewContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'contact'
        self.helper.form_method = 'post'
        self.helper.form_tag = True
        self.helper.layout = Layout(
                                    Field('email',required=True),
                                    Field('compliant_categ',required=True),
                                    Field('telephone',required=True),
                                    Field('complaint_text',required=True),
                                    Submit(name='SAVE', value='GET',type='Submit',css_class='btn btn-success'),
                                    Reset(name='RESET', value='RESET',type='Submit',css_class='btn btn-danger'))

