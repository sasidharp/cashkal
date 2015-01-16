from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import datetime
# *************************************************************************************
# Custom user manager to create and edit users                                        *
# *************************************************************************************
class MyUserManager(BaseUserManager):
    def create_user(self, email, TypeofOrg, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            TypeofOrg=TypeofOrg,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, TypeofOrg, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            TypeofOrg=TypeofOrg
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
# *************************************************************************************
# Custom user to create and edit users  EMAIL as user id                              *
# *************************************************************************************
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='EMAIL',
        max_length=255,
        unique=True,
    )
    orghelps = (('1','Individual'),('2','Organization'))

    TypeofOrg=models.CharField(max_length=1,blank=False,choices=orghelps,verbose_name='User')

    name1=models.CharField(max_length=120,null=True,blank=True,verbose_name='Name')
    name2=models.CharField(max_length=120,null=True,blank=True,verbose_name='Name2')
    name3=models.CharField(max_length=120,null=True,blank=True,verbose_name='Name3')

    first_name=models.CharField(max_length=120,null=True,blank=True,verbose_name='First Name')
    last_name=models.CharField(max_length=120,null=True,blank=True,verbose_name='Last Name')
    middle_name=models.CharField(max_length=120,null=True,blank=True,verbose_name='Middle Name')

   
    currency=models.CharField(max_length=4,verbose_name='Currency')
    corpid=models.CharField(max_length=20,verbose_name='CORP ID')
#   calpro=models.CharField(max_length=1,null=True,blank=True,verbose_name='Calendar Profile')
#   calpro1=models.CharField(max_length=1,null=True,blank=True,verbose_name='Calendar Profile')

	
    title=models.CharField(max_length=2,null=True,blank=True,verbose_name='Title')
    addr1=models.CharField(max_length=60,null=True,blank=True,verbose_name='Address Line1')
    addr2=models.CharField(max_length=60,null=True,blank=True,verbose_name='Address Line2')

    fiscal_year=models.CharField(max_length=1,null=True,blank=True,verbose_name='Fiscal')

    city=models.CharField(max_length=30,null=True,blank=True,verbose_name='City')
    pincode=models.CharField(max_length=10,null=True,blank=True,verbose_name='Pincode')
    country=models.CharField(max_length=2,null=True,blank=True,verbose_name='Country')
    mobile=models.CharField(max_length=20,null=True,blank=True,verbose_name='Mobile')
    landline=models.CharField(max_length=20,null=True,blank=True,verbose_name='Land Phone')
#   fax1=models.CharField(max_length=20,null=True,blank=True,verbose_name='FAX')

    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updatestamp=models.DateTimeField(auto_now_add=False,auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['TypeofOrg' ]


    objects = MyUserManager()
    items=models.Manager()

    def __unicode__(self):
        return (self.email)

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def get_currency(self):
        # The user is identified by their email address
        return self.currency

    def get_calop(self):
        # The user is identified by their email address
        return self.fiscal_year

    def get_corpid(self):
        # The user is identified by their email address
        if self.TypeofOrg == 1:
            return 'INDIVIDUAL'
        else:
            return self.corpid

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
# *************************************************************************************
# Custom user manager to create and edit users                                        *
# *************************************************************************************
class MYCASHFLOW(models.Model):

    id=models.AutoField(max_length=20,null=False,blank=False,primary_key=True,auto_created=True )
    parent=models.CharField(max_length=20)

    user=models.CharField(max_length=75,null=False,blank=False)
    corpid=models.CharField(max_length=20,null=False,blank=False,default='INDI')

    accepted_direction =(('I','Incoming'),('O','Expense'))
    direction=models.CharField(max_length=75,null=False,blank=False,verbose_name='Direction',choices=accepted_direction,default='O')

    categ=models.CharField(max_length=75,null=False,blank=False,verbose_name='Expense Type')

    accepted_frequency =(('M','Monthly'),
                         ('W','Weekly'),
                         ('D','Daily'),
                         ('B','Bi Weekly'),
                         ('Q','Quarterly'),
                         ('H','Half Yearly'),
                         ('Y','Yearly'),
                         ('S','Ad Hoc'))

    frequency=models.CharField(max_length=1,null=False,blank=False,verbose_name='Frequency',choices=accepted_frequency,default='C')
    fdate=models.DateField(default=datetime.date.today(), verbose_name='Date')

    amount=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Amount')
    accepted_currencies =(('USD','USD'),('INR','INR'))
    currency=models.CharField(null=False,blank=False,verbose_name='Currecny',choices=accepted_currencies,default='USD',max_length=3)

    recipient=models.CharField(max_length=75,null=True,blank=True,verbose_name='Payer/Recipient')
    name=models.CharField(max_length=75,null=True,blank=True,verbose_name='Name')

    street=models.CharField(max_length=75,null=True,blank=True,verbose_name='Street')
    city=models.CharField(max_length=75,null=True,blank=True,verbose_name='City')
    zipcode=models.CharField(max_length=10,null=True,blank=True,verbose_name='Zipcode')
    region=models.CharField(max_length=2,null=True,blank=True,verbose_name='Region')


    accepted_payments =(('C','CARD'),('W','WIRE'),('B','CASH'))
    paymethod=models.CharField(null=False,blank=False,verbose_name='Type of Payment',choices=accepted_payments,default='C',max_length=1)

    telephone=models.CharField(max_length=12,null=True,blank=True,verbose_name='TEL:')
    email=models.EmailField(null=True,blank=True)
    fax=models.CharField(max_length=12,null=True,blank=True,verbose_name='Fax')

    notes1=models.CharField(max_length=75,null=True,blank=True,verbose_name='Notes1')
    notes2=models.CharField(max_length=75,null=True,blank=True,verbose_name='Notes2')
    notes3=models.CharField(max_length=75,null=True,blank=True,verbose_name='Notes3')

    converted=models.CharField(max_length=1,null=True,blank=True,verbose_name='CONVERTED')



    items=models.Manager()

# *************************************************************************************
# expemse categ                                        *
# *************************************************************************************
class expense_categories(models.Model):

    id=models.AutoField(max_length=20,null=False,blank=False,primary_key=True,auto_created=True )
    user=models.CharField(max_length=75,null=False,blank=False)
    corpid=models.CharField(max_length=20,null=False,blank=False,default='INDI')
    description=models.CharField(max_length=75,null=False,blank=False,verbose_name='Description')

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description


    items=models.Manager()

# class types(models.Model):
#
#     user=models.CharField(max_length=75,null=False,blank=False)
#     types=models.CharField(max_length=2,null=False,verbose_name='EXPENSE CATEGORY')
#     type_desc=models.CharField(max_length=50,null=False,verbose_name='EXPENSE CATEGORY')
#
#     def __unicode__(self):
#         return self.type_desc

# class payment_type(models.Model):
#     type=models.CharField(max_length=2,null=False,verbose_name='PAYMENT TYPE')
#     type_desc=models.CharField(max_length=50,null=False,verbose_name='PAYMENT TYPE')
#
#     def __unicode__(self):
#         return self.type_desc

class cashflow_actuals(models.Model):

    id=models.AutoField(max_length=20,null=False,blank=False,primary_key=True,auto_created=True )

    user=models.CharField(max_length=75,null=False,blank=False)
    corpid=models.CharField(max_length=20,null=False,blank=False,default='INDI')


    cashflow_id=models.IntegerField(max_length=20,null=False,blank=False,default=0)

    accepted_direction =(('I','Incoming'),
                         ('O','Expense'))
    direction=models.CharField(max_length=75,null=False,blank=False,verbose_name='Direction',choices=accepted_direction,default='O')

    categ=models.CharField(max_length=75,null=False,blank=False,verbose_name='Expense Type')

    accepted_frequency =(('M','Monthly'),
                         ('W','Weekly'),
                         ('D','Daily'),
                         ('B','Bi Weekly'),
                         ('Q','Quarterly'),
                         ('H','Half Yearly'),
                         ('Y','Yearly'),
                         ('S','Ad Hoc'))

    frequency=models.CharField(max_length=1,null=False,blank=False,verbose_name='FREQUENCY',choices=accepted_frequency,default='C')
    fdate=models.DateField(default=datetime.date.today(), verbose_name='DATE')

    amount=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='AMOUNT')
    accepted_currencies =(('USD','USD'),('INR','INR'))
    currency=models.CharField(null=False,blank=False,verbose_name='CURRENCY',choices=accepted_currencies,default='USD',max_length=3)

    recipient=models.CharField(max_length=75,null=True,blank=True,verbose_name='PAYER/RECIPIENT')
    name=models.CharField(max_length=75,null=True,blank=True,verbose_name='NAME')

    street=models.CharField(max_length=75,null=True,blank=True,verbose_name='STREET')
    city=models.CharField(max_length=75,null=True,blank=True,verbose_name='CITY')
    zipcode=models.CharField(max_length=10,null=True,blank=True,verbose_name='ZIPCODE')
    region=models.CharField(max_length=2,null=True,blank=True,verbose_name='REGION')


    accepted_payments =(('C','CARD'),('W','WIRE'),('B','CASH'))
    paymethod=models.CharField(null=False,blank=False,verbose_name='TYPE OF PAYMENT',choices=accepted_payments,default='C',max_length=1)

    telephone=models.CharField(max_length=12,null=True,blank=True,verbose_name='TEL:')
    email=models.EmailField(null=True,blank=True)
    fax=models.CharField(max_length=12,null=True,blank=True,verbose_name='FAX')

    notes1=models.CharField(max_length=75,null=True,blank=True,verbose_name='NOTES1')
    notes2=models.CharField(max_length=75,null=True,blank=True,verbose_name='NOTES2')
    notes3=models.CharField(max_length=75,null=True,blank=True,verbose_name='NOTES3')

    actualamount=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='ACTUAL AMOUNT')
    acurrency=models.CharField(null=False,blank=False,verbose_name='CURRENCY',choices=accepted_currencies,default='USD',max_length=3)

    items=models.Manager()

# *************************************************************************************
# contact us                                                                          *
# *************************************************************************************
class contact(models.Model):

    id=models.AutoField(max_length=20,null=False,blank=False,primary_key=True,auto_created=True )
    user=models.CharField(max_length=75,null=False,blank=False)
    corpid=models.CharField(max_length=20,null=False,blank=False,default='INDI')

    email=models.EmailField(verbose_name='Email',max_length=255,unique=False )

    accepted_comp =      (('N','New User Registration'),
                         ( 'G','General Query'),
                         ( 'U','Issue with Login'),
                         ( 'R','Issue with Registration'),
                         ( 'X','Forgot Password'),
                         ( 'Y','Issue with transaction'),
                         ( 'Y','Feedback'),
                         ( 'S','Interested'))

    categ=models.CharField(max_length=75,null=False,blank=False,verbose_name='Service Request For',choices=accepted_comp,default='S')
    telephone=models.CharField(max_length=12,null=True,blank=True,verbose_name='Contact No:')

    complaint_text=models.TextField(verbose_name='Description')

    items=models.Manager()

# *************************************************************************************
# Muliple users                                                                       *
# *************************************************************************************
class orgusers(models.Model):

    id=models.AutoField(max_length=20,null=False,blank=False,primary_key=True,auto_created=True )
    corpid=models.CharField(max_length=20,null=False,blank=False,verbose_name='CORP ID')
    user=models.CharField(max_length=75,null=False,blank=False,verbose_name='USER')
    pin=models.CharField(max_length=4,null=False,blank=False,verbose_name='PIN')

    items=models.Manager()

