from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field ,Row,Submit , Button ,Reset
from crispy_forms.bootstrap import StrictButton, PrependedAppendedText , FormActions , StrictButton , UneditableField,\
    AppendedText , FieldWithButtons
from crispy_forms.layout import Div 
from crispy_forms.bootstrap import Tab , TabHolder
from crispy_forms.bootstrap import AppendedText,AppendedPrependedText,InlineField
from crispy_forms.templatetags.crispy_forms_field import css_class


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='ReEnter',  widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        exclude = ( 'password', )
#         fields = ('email', 'TypeofOrg')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match, please check")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'USER'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.form_class='form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        corp_text  =  'Please explain the usage - this should be entered if' + 'mutiple users from your organization would be' + 'tasked with recording these entries. Also, that this' + 'ID would used to accumulate all records entred by'
        corp_text  =  corp_text  + 'all individuals entering under the same corporate' +  'ID. The ID shouild be minimum 6 characters,' + 'alphanumeric, case sensitive and will be masked' + 'while entry'

        self.helper.layout = Layout(
                                        # TabHolder(
                                        #             Tab('',
                                                     Field('email',autofocus=True),
                                                     Field('password1',placeholder='password',required=True),
                                                     Field('password2',placeholder='Retype password',required=True),
                                                     FieldWithButtons('TypeofOrg'),
                                                     # Field('name1',placeholder='name1',required=True,css_class='form-horizontal'),
                                                     # Field('name2',placeholder='name2',required=True),
                                                     # # Field('name3',placeholder='name3',required=True),
                                                     # Field('first_name',placeholder='first name',required=True),
                                                     # Field('last_name',placeholder='last_name',required=True),
                                                     # # Field('middle_name',placeholder='middle_name',required=True),
                                                     Field('currency',placeholder='USD',required=True,title='This is defaulted for all transactions, unless changed otherwise during entry'),
                                                     Field('corpid',placeholder='six character code',required=True,title=corp_text),
                                                     # Field('title',placeholder='Mr',required=True),
                                                     # Field('fiscal_year',placeholder='year',required=True),
                                                     # Field('city',placeholder='city',required=True),
                                                     # Field('pincode',placeholder='pincode',required=True),
                                                     # Field('country',placeholder='country',required=True),
                                                     # Field('mobile',placeholder='mobile',required=True),
                                                     # Field('landline',placeholder='landline',required=True),
                                                     # Field('fax',placeholder='fax',required=True),
                                                     Submit( name='REGISTER', value='REGISTER',type='Submit',css_class='btn btn-success'),
                                                     Reset( name='RESET', value='RESET',type='Submit',css_class='btn btn-danger')

                                                # )



                                 # )
)

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'TypeofOrg', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'TypeofOrg', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('TypeofOrg',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'TypeofOrg', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)