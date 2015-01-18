from django.shortcuts import render,render_to_response , RequestContext
from .forms import *
from django.http import HttpResponse
from .models import expense_categories
from .models import MYCASHFLOW,cashflow_actuals,contact,orgusers
import jsonpickle
from django.forms import model_to_dict
import datetime
from datetime import date
from django.contrib.auth import *
from django.http.response import HttpResponseRedirect
import random
from .admin import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from .BusinessLogic import jdata ,get_occurances , fileupload
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail

#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def logout1(request):
    logout(request)
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

#**********************************************************************************************#
#                               Check if user and password is correct                          #
#**********************************************************************************************#
class AuthenticateUser(View):
    result={}
    def post(self,request):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user :
            login(request,user)
            self.result['flag'] = ''
            self.result['message'] = 'Welcome\t ' + request.user.get_short_name() + '\t!'
        else:
            self.result['flag'] = 'X'
            self.result['message']='Either Username or Password is Incorrect'

        data = jsonpickle.encode(self.result, unpicklable=False, make_refs=False, keys=False)
        return HttpResponse(data, content_type='application/json')
#**********************************************************************************************#
#                             Create the sub user                                             #
#**********************************************************************************************#
class CreateCorpUser(View):
    default_values={}
    subuser_values={}
    message = ''
    def post(self,request):

        self.default_values = request.POST.copy()
        self.default_values['corpid'] = request.user.get_corpid()
        self.default_values['TypeofOrg'] = '1'
        self.default_values['email'] =  request.POST['email']
        self.default_values['password1'] = request.POST['pin']
        self.default_values['password2'] = request.POST['pin']
        self.default_values['currency'] = request.user.get_currency()
        self.default_values['last_login'] = datetime.datetime.today()
        self.default_values['search1_tag'] = 'Initial'
        self.default_values['search2_tag'] = 'Initial'


        self.subuser_values['corpid'] = request.user.get_corpid()
        self.subuser_values['user'] = request.POST['email']
        self.subuser_values['pin']  = request.POST['pin']

        Orgform=Adduser(self.subuser_values)
        form = UserCreationForm(self.default_values)
  	
	if form.is_valid() and Orgform.is_valid():
            id= Orgform.save()
            if id:
                user = form.save()
                if user:
                    self.message = "User Added"
		    send_mail('Welcome to CASKCAL.COM', """'Please use your email id to login \n. Use PIN '{PIN}' to login'.format(request.POST['pin'])""", settings.DEFAULT_FROM_EMAIL,[request.POST['email'],])
		else:
                    self.message = "Error saving user"
            else:
                self.message = "Error adding additional user"
        else:
            self.message = form.errors


        data = jsonpickle.encode(self.message, unpicklable=False, make_refs=False, keys=False)
        return HttpResponse(data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
# Redirects the page to main login window...singup.html page
def home(request):
    form=UserCreationForm()
    if request.method=='GET':
        if 'username' in request.GET:
            username = request.GET['username']
            password = request.GET['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/calen/")
            else:
                return render_to_response('signup.html',locals(),context_instance=RequestContext(request))
    else:
        default_values = request.POST.copy()
        default_values['last_login']   = datetime.datetime.today()
        default_values['search1_tag']  = 'Initial'
        default_values['search2_tag']  = 'Initial'
        if default_values['corpid']  != "":
           default_values['corpid'] = str(default_values['corpid']).upper()
        else:
           default_values['corpid'] = 'INDIVIDUAL'

        form=UserCreationForm(default_values)
        if form.is_valid():
            form.save()
            # return render_to_response('signup.html',({'form':form},{'msg':'Registered'}),context_instance=RequestContext(request))
            user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            if user:
                login(request, user)
                send_mail('Welcome to CASKCAL.COM', "Sample mail to welcome user..Need content here ", settings.DEFAULT_FROM_EMAIL,[form.cleaned_data['email'],])
                return HttpResponseRedirect("/calen/")
            else:
                HttpResponse('our fault..will fix')
        else:
                HttpResponse(form.errors)
      
    return render_to_response("signup.html",{'form':form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
# The list of entries based on certain criteria would displayed using JQGrid. JQgrid excpects data
# in the following JSON format. JSON is formatted using JSON pickle library.

#JSON FORMAT REQUIRED BY JQGRID 
# {
#   "total": "xxx",
#   "page": "yyy",
#   "records": "zzz",
#   "rows" : [
#     {"id" :"1", "cell" :["cell11", "cell12", "cell13"]},
#     {"id" :"2", "cell":["cell21", "cell22", "cell23"]},
#       ...
#   ]
# }
@login_required(login_url='/home/')
def cashlist(request):
#   create an array to hold the table data  
    rows=[]

#   get the records from the MYCASHFLOW table
    if( 'A' in request.GET and 'D' in request.GET ):
        raw_sql="""select * from user_mycashflow where fdate ='{today_date}' and "user" ='{username}' and direction = '{direction}'""".format(today_date=request.GET['D'],username=request.user,direction=request.GET['A'])
    elif( 'L' in request.GET ):
        raw_sql="""select * from user_mycashflow where fdate ='{today_date}' and "user" ='{username}'""".format(today_date=request.GET['D'],username=request.user)
    else:
        raw_sql="""SELECT * FROM user_mycashflow where "user" = '{username}' and parent = 'P'""".format(today_date=datetime.date.today(),username=request.user)

    row_list = MYCASHFLOW.items.raw(raw_sql)
#   append them into row
    total=1
    for row_item in row_list:
        row_dict = model_to_dict(row_item, (), ())
#   Append to the row list
        if row_dict['direction'] == 'I':
            row_dict['direction'] = 'Inflow'
        elif row_dict['direction'] == 'O':
            row_dict['direction'] = 'Outflow'
        row_dict['amount'] = row_dict['amount'].__str__()
        total=total+1
        rows.append(row_dict)   
    pages=1
    records=total
    json_data = jdata(total, pages, records, rows)
    
    data = jsonpickle.encode(json_data, unpicklable=False, make_refs=False, keys=False)
    return HttpResponse(data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def actuallist(request):
#   create an array to hold the table data
    rows=[]
#   get the records from the MYCASHFLOW table
#   get the records from the MYCASHFLOW table
    if( 'A' in request.GET and 'D' in request.GET ):
        raw_sql="""select * from user_cashflow_actuals where fdate ='{today_date}' and "user" ='{username}' and direction = '{direction}'""".format(today_date=request.GET['D'],username=request.user,direction=request.GET['A'])
    elif( 'L' in request.GET ):
        raw_sql="""select * from user_cashflow_actuals where fdate ='{today_date}' and "user" ='{username}'""".format(today_date=request.GET['D'],username=request.user)
    else:
        raw_sql="""SELECT * FROM user_cashflow_actuals where "user" = '{username}'""".format(today_date=datetime.date.today(),username=request.user)
#   append them into row
    row_list = cashflow_actuals.items.raw(raw_sql)
    total=1
    for row_item in row_list:
        row_dict = model_to_dict(row_item, (), ())
#   Append to the row list
        if row_dict['direction'] == 'I':
            row_dict['direction'] = 'Inflow'
        elif row_dict['direction'] == 'O':
            row_dict['direction'] = 'Outflow'

        row_dict['amount'] = row_dict['actualamount']
        row_dict['amount'] = row_dict['amount'].__str__()

        total=total+1
        rows.append(row_dict)
    pages=1
    records=total
    json_data = jdata(total, pages, records, rows)

    data = jsonpickle.encode(json_data, unpicklable=False, make_refs=False, keys=False)
    return HttpResponse(data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def categories(request):

    rows=[]
    rows.append({'description':'Rent'})
    rows.append({'description':'Subscription'})
    rows.append({'description':'Office'})
    rows.append({'description':'Expenses'})
    rows.append({'description':'Meals'})
    rows.append({'description':'Snacks'})
    row_list = expense_categories.items.filter(user=request.user)
    for row_item in row_list:
        row_dict = model_to_dict(row_item, (), ())
        rows.append(row_dict)
    data = jsonpickle.encode(rows, unpicklable=False, make_refs=False, keys=False)
    return HttpResponse(data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def cashactuals(request):
    
    msg=''
    errors={} 
    formdate={}
    default_values={}
    no_render=''
    if request.method=='POST':
        if 'id' in request.GET:
            
            actual_item = MYCASHFLOW.items.get(id=request.GET['id'])
        
            default_items                   = model_to_dict(actual_item)
            
            default_items['user']           = request.user
            default_items['corpid']         = request.user.get_corpid()
            default_items['cashflow_id']    = request.GET['id']
            default_items['actualamount']   = request.POST['actualamount']
            default_items['acurrency']      = request.user.get_currency()
            default_items['notes2']         = request.POST['notes2']
            default_items['notes3']         = request.POST['notes3']

            form = ActualForm(default_items,initial=({'user':request.user,'currency':default_items['currency']}))
        
        else:
            
            default_items = request.POST.copy()
            default_items['user']               = request.user
            default_items['corpid']             = request.user.get_corpid()
            default_items['amount']             = "0.01"
            default_items['currency']           = request.user.get_currency()
            default_items['acurrency']          = request.user.get_currency()
            default_items['frequency']          = "W"
            default_items['fdate']              = datetime.date.today()
            default_items['cashflow_id']        = random.randint(90000, 99999)


            form = ActualForm(default_items,initial=({'user':request.user,'currency':default_items['currency']}))



        if form.is_valid():
            saved_item = form.save()
            try:
                actual_item.notes1=datetime.date.today().__str__()
                actual_item.save()
            except:
                pass
            if 'L' in request.GET:
                return HttpResponseRedirect("/launcher/")
            else:
                msg='Entry Saved'
                return render_to_response('actual.html',({'form': form,'msg':msg}),context_instance=RequestContext(request))
        else:
            msg=form.errors    
            return render_to_response('actual.html',({'form': form,'msg':msg}),context_instance=RequestContext(request))
    else:       
        
        if 'id' in request.GET:
            
            id_to_display = request.GET['id']
            
            formdata      =  MYCASHFLOW.items.get(id=id_to_display)
            
            initial_values                  =model_to_dict(formdata)
            initial_values['actualamount']  =initial_values['amount']
            initial_values['acurrency']     =request.user.get_currency()
            initial_values['notes1']        =id_to_display

            form = ActualForm(initial_values,initial=({'user':request.user,'corpid':request.user.get_corpid(),'currency':initial_values['currency']}))
            return form

        elif 'D' in request.GET:
            form=cashflow_actuals.items.get(id=request.GET['D'])
            cashflow_item=MYCASHFLOW.items.get(id=form.cashflow_id)
            cashflow_item.converted = ''
            form.delete()
            cashflow_item.save()
            return HttpResponse('Deleted')
        elif 'M' in request.GET:
            instance=cashflow_actuals.items.get(id=request.GET['M'])
            intial_values   =   model_to_dict(instance)
            form=ActualForm(initial=intial_values)
            return render_to_response('actual.html',({'form': form,'msg':msg}),context_instance=RequestContext(request))

        else:
            form = ActualForm(initial=({'user':request.user,'corpid':request.user.get_corpid(),'currency':request.user.get_currency()}))
            
        return render_to_response('actual.html', {'form': form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def cash(request):
    form = NewCashForm(initial=({'user':request.user,'currency':request.user.get_currency()}))
    if request.method=='POST':
        default_values                = request.POST.copy()
        default_values['user']        = request.user.get_short_name()
        default_values['corpid']      = request.user.get_corpid()
        default_values['parent']      ='P'
        default_values['currency']    = request.user.get_currency()
        default_values['categ']       = request.POST['category']


        form = NewCashForm(default_values)
        
        if form.is_valid():
                id=form.save()
                msg='Entry Saved'
                if form.cleaned_data['frequency'] != 'S':
                    create_forecasted_entries(form,id,request)
                return HttpResponseRedirect("/calen/")
        else:
            msg=form.errors
            errors = form.errors
        
        return render_to_response('cash.html',({'form': form,'msg':msg}),context_instance=RequestContext(request))
    
    else:
        if 'N' in request.GET:
            
            form        =   MYCASHFLOW.items.get(id=request.GET['N'])
            dict        =   model_to_dict(form)
            dict['id']  =   ''
            form=NewCashForm(dict)
            return render_to_response('cash.html', {'form': form},context_instance=RequestContext(request))
        
        elif 'D' in request.GET:
        
            form        =   MYCASHFLOW.items.get(id=request.GET['D'])
            form.delete()
            forms       =   MYCASHFLOW.items.filter(parent=request.GET['D'],converted__isnull=True)
            for item in forms:
                item.delete()
            return HttpResponse('Deleted')
        elif 'M' in request.GET:
            
            instance        =   MYCASHFLOW.items.get(id=request.GET['M'])
            intial_values   =   model_to_dict(instance)
            form            =   NewCashForm(intial_values)
            return render_to_response('cash.html', {'form': form},context_instance=RequestContext(request))

    return render_to_response('cash.html', ({'form': form}),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def events(request):
 # ************************************************************************************************
# ************************************************************************************************
    from django.db import connection
    calendar_final=[]
    event_list=[]
    found=''
# ************************************************************************************************
    raw_stmt ="""select fdate  ,  amount  , direction from user_mycashflow where "user" = '{user_name}' and converted != 'X' order by fdate """.format(user_name=request.user)
    cursor = connection.cursor()
    cursor.execute(raw_stmt)
    calendar_cash_items = cursor.fetchall()
# ************************************************************************************************
    raw_stmt ="""select fdate  ,  actualamount  , direction from user_cashflow_actuals where "user" = '{user_name}' order by fdate""".format(user_name=request.user)
    cursor = connection.cursor()
    cursor.execute(raw_stmt)
    calendar_actual_items = cursor.fetchall()
#************************************************************************************************
#************************************************************************************************
    cnt = 0
    planned_dict={}
    actual_dict={}
    final_record = 0
    planned_in=0
    planned_out=0
    actual_in=0
    actual_out=0
    if calendar_cash_items.__len__() > 0 :
        first_item = calendar_cash_items[0]
        tmpdate= first_item[0]
        final_record = calendar_cash_items.__len__()
        for item in calendar_cash_items:
            cnt = cnt + 1
            if tmpdate!=item[0]:
                if planned_in != 0:
                    dict={'title':'Income:' + str(planned_in),'start':tmpdate.isoformat(),'color':'#C00000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=I'+'&T'+'=P'}
                    event_list.append(dict.copy())
                if planned_out != 0:
                    dict={'title':'Expense:' + str(planned_out),'start':tmpdate.isoformat(),'color':'#C00000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=O'+'&T'+'=P'}
                    event_list.append(dict.copy())
                planned_in=0
                planned_out=0
                tmpdate = item[0]

            if item[2] == 'I':
                planned_in   = planned_in + item[1]
            else:
                planned_out   = planned_out + item[1]

            if cnt == final_record:
                if planned_in != 0:
                    dict={'title':'Income:' + str(planned_in),'start':tmpdate.isoformat(),'color':'#C00000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=I'+'&T'+'=P'}
                    event_list.append(dict.copy())
                if planned_out != 0:
                    dict={'title':'Expense:' + str(planned_out),'start':tmpdate.isoformat(),'color':'#C00000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=O'+'&T'+'=P'}
                    event_list.append(dict.copy())
                cnt = 0
# ************************************************************************************************
# ************************************************************************************************
    if calendar_actual_items.__len__() > 0 :
        first_item = calendar_actual_items[0]
        tmpdate= first_item[0]
        final_record = calendar_actual_items.__len__()
        cnt = 0
        for item in calendar_actual_items:
            cnt = cnt + 1
            if tmpdate!=item[0]:
                if actual_in != 0:
                    dict={'title':'Income:' + str(actual_in),'start':tmpdate.isoformat(),'color':'#008000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=I'+'&T'+'=A'}
                    event_list.append(dict.copy())
                if actual_out != 0:
                    dict={'title':'Expense:' + str(actual_out),'start':tmpdate.isoformat(),'color':'#008000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=O'+'&T'+'=A'}
                    event_list.append(dict.copy())
                actual_in=0
                actual_out=0
                tmpdate = item[0]

            if item[2] == 'I':
                actual_in   = actual_in + item[1]
            else:
                actual_out   = actual_out + item[1]

            if cnt == final_record:
                if actual_in != 0:
                    dict={'title': 'Income:' + str(actual_in),'start':tmpdate.isoformat(),'color':'#008000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=I'+'&T'+'=A'}
                    event_list.append(dict.copy())
                if actual_out != 0:
                    dict={'title': 'Expense:' + str(actual_out),'start':tmpdate.isoformat(),'color':'#008000','url':'/launcher/?D='+tmpdate.isoformat()+'&A'+'=O'+'&T'+'=A'}
                    event_list.append(dict.copy())
                actual_in=0
                actual_out=0
                cnt = 0
    json_data=jsonpickle.encode(event_list, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def convertactual(request):
    result={}
    try:
        cashflow_item = MYCASHFLOW.items.get(id=request.POST['id'])
    except(RuntimeError):
        result['error'] = 'Data inconistency-check with admin'

    if cashflow_item is None:
        result['error'] = 'cashflow does not exist'
    else:
        default_fields = model_to_dict(cashflow_item)
        default_fields['actualamount']   = request.POST['actualamount']
        default_fields['acurrency']      = request.user.get_currency()
        default_fields['cashflow_id']    = request.POST['cashflow_id']
        default_fields['corpid']         = request.user.get_corpid()
        default_fields['user']           = request.user
        form = ModalActualForm(default_fields)
        if form.is_valid():
            form.save()
            cashflow = MYCASHFLOW.items.get(id=request.POST['cashflow_id'])
            if cashflow is not None:
                cashflow.converted = 'X'
                cashflow.save()
            else:
                result['error'] = 'cashflow not updated'
            result['success'] = 'X'
        else:
            result['error'] = form.errors
    json_data=jsonpickle.encode(result, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def calenoption(request):
    if 'calop' in request.GET:
         myuser = request.user
         myuser.fiscal_year=request.GET['calop']
         myuser.save()
         return HttpResponse('saved')
    else:
        calop=request.user.get_calop()
        return HttpResponse(calop)
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def calendar(request):

    return render_to_response('calendar.html',{'user_option':request.user.get_calop()},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def corrections(request):
#     items=MYCASHFLOW.items.all()
    # return render(request,"cash.html",{'form':cash})
    # return render(request,"launcher.html",{'form':cash})
    return render(request,"categ.html",{'MYCASHFLOW':MYCASHFLOW.items.all()})
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def newcateg(request):
    Message=False
    if request.method == 'POST':
        form=NewExpenseCategoryForm(request.POST)
        if form.is_valid():
            newcateg = form.save()
        Message="Database Updated"
        return HttpResponseRedirect("/categ/")
    else:
        form=NewExpenseCategoryForm()
#       return render_to_response('categ.html', {'form':form},context_instance=RequestContext(request))
        return render_to_response('categ.html', {'form':form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def addcateg(request):
    msg=False
    errors={}
    if request.method == 'POST':
        default_values = request.POST.copy()
        default_values['user']=request.user
        default_values['corpid']= request.user.get_corpid()
        form=NewExpenseCategoryForm(default_values)
        if form.is_valid():
            newcateg = form.save()
            return HttpResponseRedirect("/cash/")
        return render_to_response('addcateg.html',({'form': form}),context_instance=RequestContext(request))
    else:
        form=NewExpenseCategoryForm( )
        return render_to_response('addcateg.html', {'form':form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def launcher(request):
    form = ModalActualForm()
    expense = "N"
    type = ""
    if 'A' in request.GET:
        expense = request.GET['A']
    if 'T' in request.GET:
        type = request.GET['T']
    return render_to_response("launcher.html", {'date':datetime.date.today(),'form':form , 'clkdate':request.GET['D'],'expense':expense,'type':type},context_instance=RequestContext(request))

#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def contact(request):
    return render_to_response("contact.html",locals(),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def pie(request):
    # select  sum(amount) as monthval , strftime('%m',fdate) as month from user_mycashflow group by strftime('%m',fdate)
    form = PieSelection( )
    if request.method == 'POST':
        return render_to_response("pie.html",context_instance=RequestContext(request))
    else:
        return render_to_response("pie.html",{'forms':form},context_instance=RequestContext(request))

#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def contact(request):
    form = NewContactForm()
    if request.method == 'POST':
        default_values = request.POST.copy()
        default_values['user']=request.user
        default_values['corpid']= request.user.get_corpid()
        form = NewContactForm(default_values)
        if form.is_valid():
            form.save()
            msg='Thank you. Request will be addressed in a weeks time'
            return render_to_response("contact.html",{'form':form,'msg':msg},context_instance=RequestContext(request))
        else:
            msg='Form could not submitted.please reach our call center @ dkdkdk'
            return render_to_response("contact.html",{'form':form,'msg':msg},context_instance=RequestContext(request))
    else:
        return render_to_response("contact.html",{'form':form},context_instance=RequestContext(request))

#**********************************************************************************************#
#                               Add user              .                                        #
#**********************************************************************************************#
class ViewAddUser(View):
    form = Adduser()
    def get(self,request):
        return render_to_response("userlist.html",{'form':self.form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Add user              .                                        #
#**********************************************************************************************#
class ViewUserList(View):
    #Variable to return the errors
    success = 'X'
    #Default values for user to be created
    default_values={}

    #Get all the users assigned for the main user
    def get(self, request):
        # No of users
        user={}
        users=[]
        for each_user in orgusers.items.filter(corpid=request.user.get_corpid()):
            user = model_to_dict(each_user, (), ())
            users.append(user)

        data = jsonpickle.encode(users, unpicklable=False, make_refs=False, keys=False)
        return HttpResponse(data, content_type='application/json')

    #Create the user delegate for the main user.
    def post(self, request):
        # Set the defaults
        self.__setdefaults__(request)
        # Create the user
        form = UserCreationForm(self.default_values)
        # Create user in Myuser !
        if form.is_valid():
            form.save()
            self.success = 'X'
        else:
            self.success = form.errors
        # Return the data in json format
        data = jsonpickle.encode(self.success, unpicklable=False, make_refs=False, keys=False)
        return HttpResponse(data, content_type='application/json')

    #Set the default values for the user
    def __setdefaults__(self,request):

        self.default_values = request.POST.copy()
        self.default_values['corpid'] = request.user.get_corpid()
        self.default_values['password2'] = request.user['password1']
        self.default_values['TypeofOrg'] = 'O'
        self.default_values['currency'] = request.user.get_currency()

#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def register(request):
    if request.method=='POST':
        default_values=request.POST.copy()
        
        if 'name1' in request.POST:
            default_values['search2_tag'] = default_values['name1']
        else:
            default_values['search2_tag'] = "A"
        
        if 'first_name' in request.POST:
            default_values['search1_tag'] = default_values['first_name']
        else:
            default_values['search1_tag'] = "B"
        
        default_values['last_login']  = datetime.datetime.today()
        
        form=UserCreationForm(default_values)
        
        if form.is_valid():
            my_user = form.save() 
#             my_user.set_password()
# #             my_user.save()
            return HttpResponseRedirect("/home/")
        else:
            return render_to_response('register.html', ({'form': form, 'msg':form.errors}),context_instance=RequestContext(request))
    form = UserCreationForm()
    return render_to_response('register.html', {'form': form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
class report_item:
    def __init__(self,date,line):
        self.adate=date
        self.line=line

@login_required(login_url='/home/')
def report(request):
    sum=cnt=0
    diff=0
    running_plan=0
    running_act=0
    actual_amount=0                    
    dailyitems=[]
    if request.method == 'POST':
        if ( request.POST['category_id'] != ""):
            row_data = MYCASHFLOW.items.filter(categ=request.POST['category_id'],
                                               fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'],
                                               user=request.user)
        else:
            row_data = MYCASHFLOW.items.filter(fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'],
                                               user=request.user)


        for rows in row_data:
            item={}
            if rows.direction == 'I':
                rows.amount = 1 * rows.amount
            else:
                rows.amount = -1 * rows.amount

            if rows.converted == 'X':
                actual_entry=cashflow_actuals.items.get(cashflow_id=rows.id)
                item['id']=rows.id
                item['adate']=actual_entry.fdate
                item['categ']=actual_entry.categ
                item['amount']=rows.amount
                if actual_entry.direction == 'I':
                    actual_entry.actualamount = 1 * actual_entry.actualamount
                else:
                    actual_entry.actualamount = -1 * actual_entry.actualamount
                item['actualamount']=actual_entry.actualamount
                xitem = report_item(item['adate'],item.copy())
                dailyitems.append(xitem)
            else:
                item['id']=rows.id
                item['adate']=rows.fdate
                item['amount']=rows.amount
                item['categ']=rows.categ
                xitem = report_item(item['adate'],item.copy())
                dailyitems.append(xitem)

        dailyitems.sort(key=lambda x: x.adate, reverse=False)
        for item_lines in dailyitems:
            if 'amount' in item_lines.line: running_plan = running_plan + item_lines.line['amount']
            if 'actualamount' in item_lines.line: running_act  = running_act + item_lines.line['actualamount']
            diff = running_plan - running_act
            item_lines.line['plan']  = running_plan
            item_lines.line['act']   = running_act
            item_lines.line['diff']  = diff
        final_items=[]
        for items in dailyitems:
            final_items.append(items.line)

        return render_to_response("dailyreport.html",{'dailyitems':final_items},context_instance=RequestContext(request))
    else:
        if not 'today' in request.GET:
            form = ReportSelection( )
            return render_to_response("dailyreport.html",{'forms':form },context_instance=RequestContext(request))
        else:
            items=MYCASHFLOW.items.filter(fdate=request.GET['today'],
                                          user=request.user)
            for item in items:
                row={'id':item.id,'date':item.fdate,'categ':item.categ,'amount':item.amount,'class':'line'}
                dailyitems.append(row)
            return render_to_response("dailyreport.html",{'dailyitems':dailyitems},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartdata(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (categ) categ  , id  , (select SUM(amount) from user_mycashflow where categ = a.categ and "user" = '{user}' and direction = 'I') as value from user_mycashflow
                    as a where "user" = '{user}' group by  categ , id order by categ""".format(user=request.user)
    row_data = MYCASHFLOW.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))
    
    for row in row_data:
        cell_data=[]
        cell_data.append({'v':row.categ})
        if row.value is not None:
            cell_data.append({'v':int(row.value)})
        else:
            cell_data.append({'v': 0})
        chart_rows_data.append({'c':cell_data})
        
    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartdata_out(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (categ) categ  , id  , (select SUM(amount) from user_mycashflow where categ = a.categ and "user" = '{user}' and direction = 'O') as value from user_mycashflow
                    as a where "user" = '{user}' group by  categ , id order by categ""".format(user=request.user)
    row_data = MYCASHFLOW.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))

    for row in row_data:
        cell_data=[]
        cell_data.append({'v':row.categ})
        if row.value is not None:
            cell_data.append({'v':int(row.value)})
        else:
            cell_data.append({'v': 0})
        chart_rows_data.append({'c':cell_data})

    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartactual(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (categ) categ  , id  , (select SUM(actualamount) from user_cashflow_actuals where categ = a.categ and "user" = '{user}' and direction = 'I') as value from user_cashflow_actuals
                    as a where "user" = '{user}' group by  categ , id order by categ""".format(user=request.user)
    row_data = cashflow_actuals.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))

    for row in row_data:
        cell_data=[]
        cell_data.append({'v':row.categ})
        if row.value is not None:
            cell_data.append({'v':int(row.value)})
        else:
            cell_data.append({'v': 0})
        chart_rows_data.append({'c':cell_data})

    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartactual_out(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (categ) categ  , id  , (select SUM(actualamount) from user_cashflow_actuals where categ = a.categ and "user" = '{user}' and direction = 'O') as value from user_cashflow_actuals
                    as a where "user" = '{user}' group by  categ , id order by categ""".format(user=request.user)
    row_data = cashflow_actuals.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))

    for row in row_data:
        cell_data=[]
        cell_data.append({'v':row.categ})
        if row.value is not None:
            cell_data.append({'v':int(row.value)})
        else:
            cell_data.append({'v': 0})
        chart_rows_data.append({'c':cell_data})

    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def chartbydirection(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (direction) direction  , id  , (select SUM(amount) from user_mycashflow where direction = a.direction and "user" = '{user}') as value from user_mycashflow
                    as a where "user" = '{user}' group by  direction , id order by direction""".format(user=request.user)
    row_data = MYCASHFLOW.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'Cash Inflow'}))
    chart_cols_data.append(({'type':'number','label':'Total'}))
    
    for row in row_data:
        cell_data=[]
        if row.direction == 'I':
            row.direction = 'Inflow'
        else:
            row.direction = 'Expenses'
        cell_data.append({'v':row.direction})
        cell_data.append({'v':str(row.value)})
        chart_rows_data.append({'c':cell_data})
        
    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')

#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def trend(request):
    from django.db import connection
    import calendar
    chart_data={}
    json_data= "none"
    item={}
    summed_list=[]
    cursor = connection.cursor()
    raw_sql=("""select direction ,extract(month from fdate) as month,extract(year from fdate) as yyyy,sum(amount) as monthval from user_mycashflow where "user" = '{user}' and fdate <='{date}' group by 1,2,3 order by 3,2 """).format(user=request.user,date=datetime.date.today())
    cursor.execute(raw_sql)
    row_data = cursor.fetchall()

    cursor = connection.cursor()
    raw_sql=("""select direction ,extract(month from fdate) as month,extract(year from fdate) as yyyy,sum(amount) as monthval from user_cashflow_actuals where "user" = '{user}' and fdate <='{date}' group by 1,2,3 order by 3,2 """).format(user=request.user,date=datetime.date.today())
    cursor.execute(raw_sql)
    row_actual_data = cursor.fetchall()

    cnt = 0
    for row in row_data:
        month = row[1]
        if cnt == 0:
            initial =   row[1]

        if initial != month:
            summed_list.append(item.copy())
            initial = month

        item['month'] = calendar.month_name[int(month)]
        if row[0] == 'I':
            item['planned_incoming'] = row[3]
        else:
            item['planned_outgoing'] = row[3]

    for row in row_actual_data:
        month = row[1]
        item['month'] = calendar.month_name[int(month)]
        if row[0] == 'I':
            item['actual_incoming'] = row[3]
        else:
            item['actual_outgoing'] = row[3]
        summed_list.append(item.copy())



    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]

    chart_cols_data.append(({'type':'string','label':'Year'}))
    chart_cols_data.append(({'type':'number','label':'Planeed'}))
    chart_cols_data.append(({'type':'number','label':'Actual'}))

    for row in summed_list:
        cell_data=[]
        cell_data.append({'v':row['month']})
        if 'planned_incoming' in row:
            cell_data.append({'v':int(row['planned_incoming'])})
        if 'planned_outgoing' in row:
            cell_data.append({'v':int(row['planned_outgoing'])})
        # cell_data.append({'v':row[0]})
        chart_rows_data.append({'c':cell_data})
    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
    # data={'cols':chart_cols_data,'rows':chart_rows_data}
    data={'cols':chart_cols_data,'rows':chart_rows_data}
    json_data=jsonpickle.encode(data, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def fill_week1():
    lweek = []
    lweek.append("1-sep")
    lweek.append("1-sep")
    lweek.append("1-sep")
    lweek.append("1-sep")
    lweek.append("1-sep")
    lweek.append("1-sep")
    lweek.append("1-sep")
    return  lweek
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def convertmodel_json(items):
    content_json="json here";
    return content_json

# Not a good way to save one by one..for the time being
def create_forecasted_entries(l_form , l_id , l_request):
     forecasted_dates = get_occurances(l_form.cleaned_data['frequency'],l_form.cleaned_data['fdate'],120)
     for date in forecasted_dates:
         forecasted_entry=MYCASHFLOW.items.create(categ=l_form.cleaned_data['category'],
                                                      user=l_request.user  ,
                                                      parent=l_id.id,
                                                      direction=l_form.cleaned_data['direction'],
                                                      frequency=l_form.cleaned_data['frequency'],
                                                      fdate=date,
                                                      amount=l_form.cleaned_data['amount'],
                                                      currency=l_form.cleaned_data['currency'],
                                                      recipient=l_form.cleaned_data['recipient'],
                                                      name=l_form.cleaned_data['name'],
                                                      street=l_form.cleaned_data['street'],
                                                      city=l_form.cleaned_data['city'],
                                                      zipcode=l_form.cleaned_data['zipcode'],
                                                      region=l_form.cleaned_data['region'],
                                                      paymethod=l_form.cleaned_data['paymethod'],
                                                      telephone=l_form.cleaned_data['telephone'],
                                                      email=l_form.cleaned_data['email'],
                                                      fax=l_form.cleaned_data['fax'],
                                                      notes1=l_form.cleaned_data['notes1'],
                                                      notes2=l_form.cleaned_data['notes2'],
                                                      notes3=l_form.cleaned_data['notes3'])
         
     
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def upload(request):
    cnt=0
    scnt=0
    ecnt=0
    fileobj=None
    fileobj = fileupload()
    if request.method == 'POST':
        if 'file' in request.FILES:
            fileobj.read_file(request.FILES['file'])
            if fileobj.errors.__len__() == 0:
                budget_table=fileobj.get_budget_table()
                categ_table=fileobj.get_categ_table()
                if ( categ_table.__len__() == 0 or budget_table.__len__() == 0 ):
                    message = 'Error uploading file.Please log issue with service desk'
                else:
                    category_instance = None
                    category = None
                    result = None
                    for eachcateg in categ_table:
                        #First record is header , not required
                        cnt = cnt + 1
                        if cnt == 1:
                            continue
                        category = eachcateg[0]
                        category_instance = expense_categories(user=request.user.get_short_name(),corpid=request.user.get_corpid(),description=category)
                        try:
                            category_instance.save()
                            result=category_instance.id
                        except(Exception):
                            result = None
                        if result == '' :
                            ecnt = ecnt + 1
                        else:
                            scnt = scnt + 1
                    status={}
                    message = 'Total' + str(cnt-1) + '  ' + 'Success' + str(scnt) + ' ' + 'Error' + ' ' + str(ecnt)
                    if ecnt == 0:
                            #Directon,category,frequency,fdate,amount,currency,recipient name street city zipcode region paymethod telephone email fax notes1  notes2 notes3
                            cnt = 0
                            for eachcashflow in budget_table:
                            #First record is header , not required
                                cnt = cnt + 1
                                if cnt == 1:
                                    continue
                                direction=eachcashflow[0]
                                category=eachcashflow[1]
                                frequency=eachcashflow[2]
                                fdate=eachcashflow[3]
                                amount=eachcashflow[4]
                                currency=eachcashflow[5]
                                recipient=eachcashflow[6]
                                name=eachcashflow[7]
                                street=eachcashflow[8]
                                city=eachcashflow[9]
                                zipcode=eachcashflow[10]
                                region=eachcashflow[11]
                                paymethod=eachcashflow[12]
                                telephone=eachcashflow[13]
                                email=eachcashflow[14]
                                fax=eachcashflow[15]
                                notes1=eachcashflow[16]
                                notes2=eachcashflow[17]
                                notes3=eachcashflow[18]

                                dict={}
                                dict['user']          = request.user.get_short_name()
                                dict['parent']        = 'P'
                                dict['corpid']        = request.user.get_corpid()
                                dict['direction']     = direction[0].upper()
                                dict['categ']      = category.strip().upper()
                                dict['frequency']     = frequency[0].strip().upper()
                                dict['fdate']         = fdate
                                dict['amount']        = int(amount)
                                dict['currency']      = request.user.get_currency()
                                dict['recipient']     = recipient.strip().upper()
                                dict['name']          = name.strip().upper()
                                dict['street']        = street.strip().upper()
                                dict['city']          = city.strip().upper()
                                dict['zipcode']       = zipcode.strip().upper()
                                dict['region']        = region.strip().upper()
                                dict['paymethod']     = paymethod[0].strip().upper()
                                dict['telephone']     = telephone.strip().upper()
                                dict['email']         = email.strip().upper()
                                dict['fax']           = fax.strip().upper()
                                dict['notes1']        = notes1.strip().upper()
                                dict['notes2']        = notes2.strip().upper()
                                dict['notes3']        = notes3.strip().upper()
                                dict['converted']     = ''

                                cash_instance = MYCASHFLOW(**dict.copy())
                                try:
                                    result = None
                                    cash_instance.save()
                                    result=cash_instance.id
                                except(Exception):
                                    result = None
                                if result == None :
                                    ecnt = ecnt + 1
                                    status[cnt]= 'F'
                                else:
                                    status[cnt]= 'S'
                                    scnt = scnt + 1

                            if ecnt == 0:
                                message = 'catgeroy and cashflows loaded succesfully'
                            else:
                                message = 'Rectify errors in cashflow'
                            return render_to_response("upload.html",{'message':message ,'status':status},context_instance=RequestContext(request))
    else:
        form = FileUpload( )
        return render_to_response("upload.html",{'form':form},context_instance=RequestContext(request))
     
     
@login_required(login_url='/home/')
def delete(request):
    MYCASHFLOW.items.filter(user=request.user.get_short_name()).delete()
    return HttpResponse('Y', content_type='application/json')
@login_required(login_url='/home/')
def adelete(request):
    cashflow_actuals.items.filter(user=request.user.get_short_name()).delete()
    return HttpResponse('Y', content_type='application/json')
