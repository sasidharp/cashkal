from weakref import finalize
from django.shortcuts import render,render_to_response , RequestContext, _get_queryset
from pip._vendor.distlib._backport.tarfile import calc_chksums
from .forms import MyModelForm,NewCashForm ,NewExpenseCategoryForm
from .forms import NewActualForm,PieSelection
from .models import cashflow_actuals
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.forms import forms
from .models import expense_categories
from .models import MYCASHFLOW,cashflow_actuals
from crispy_forms.templatetags import crispy_forms_tags
from django.forms.models import modelformset_factory
from django.core import serializers
from http.client import HTTPResponse
import jsonpickle
from jsonpickle import pickler
from django.forms import model_to_dict
from user.BusinessLogic import jdata, get_occurances, jevent
from user.forms import ReportSelection, NewUserReg , ActualForm , NewUser
import datetime
from datetime import date
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import *
from django.http.response import HttpResponseRedirect
import random
from .admin import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
import calendar
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def logout1(request):
    logout(request)
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
# Redirects the page to main login window...singup.html page
def home(request):
    if request.method=='GET':
        if 'username' in request.GET:
            username = request.GET['username']
            password = request.GET['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/launcher/")
            else:
                return HttpResponseRedirect("/register/")
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))
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
    today_date = date.isoformat(datetime.date.today());
    raw_sql="SELECT * FROM user_mycashflow where fdate <= '{today_date}' and notes1 = '' and user = '{username}'".format(today_date=today_date , username=request.user)
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
    row_list = cashflow_actuals.items.all()
#   append them into row
    total=1
    for row_item in row_list:
        row_dict = model_to_dict(row_item, (), ())
#   Append to the row list
        total=total+1
        rows.append(row_dict)   
        pages=1
    records=total
   
    json_data = jdata(total, pages, records, rows) 
    
    data = jsonpickle.encode(json_data, unpicklable=False, make_refs=False, keys=False)
    return HttpResponse(data, content_type='application/json')
#     cash_formset = modelformset_factory(MYCASHFLOW,can_order=True,can_delete=True)
#     formset = cash_formset(queryset=MYCASHFLOW.items.all())
#     return render_to_response('cashlist.html', {'formset': formset})
#     return render_to_response('list.html',{'json':data})
#     return  HttpResponse(data,content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def cashactuals(request):
    
    msg=''
    errors={} 
    formdate={}
    default_values={}
    
    if request.method=='POST':
        if 'id' in request.GET:
            
            actual_item = MYCASHFLOW.items.get(id=request.GET['id'])
        
            default_items                   = model_to_dict(actual_item)
            
            default_items['user']          = request.user
            default_items['corpid']        = '123' 
            default_items['cashflow_id']    = request.GET['id']
            default_items['actualamount']   = request.POST['actualamount']
            default_items['acurrency']      = request.user.get_currency()
            default_items['notes2']         = request.POST['notes2']
            default_items['notes3']         = request.POST['notes3']
                
            form = ActualForm(default_items,initial=({'user':request.user,'currency':default_items['currency']}))
        
        else:
            
            default_items = request.POST.copy()
            default_items['user']        = request.user
            default_items['corpid']      = '123' 
        
            default_items['amount']             = "0.01"
            default_items['currency']           = request.user.get_currency()
            default_items['acurrency']      = request.user.get_currency()
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
                msg='Entry recoreded'    
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
            initial_values['acurrency']     =initial_values['currency']
            initial_values['notes1']        =id_to_display
            
            form = ActualForm(initial_values,initial=({'user':request.user,'currency':initial_values['currency']}))
        else:
            form = ActualForm(initial=({'user':request.user,'currency':request.user.get_currency()}))
            
        return render_to_response('actual.html', {'form': form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def cash(request):
    msg=''
    form = NewCashForm(initial=({'user':request.user,'currency':request.user.get_currency()}))
    errors={}
    if request.method=='POST':
        default_values                = request.POST.copy()
        default_values['user']        = request.user
        default_values['corpid']      = '123'
        default_values['parent']      ='P'
        default_values['currency']    = request.user.get_currency()
       
        form = NewCashForm(default_values)
        
        if form.is_valid():
                id=form.save()
                msg='Entry Saved'
                create_forecasted_entries(form,id,request)
                form = NewCashForm()
        else:   
            msg=form.errors
            errors = form.errors
        
        return render_to_response('cash.html',({'form': form,'errors':errors,'msg':msg}),context_instance=RequestContext(request))
    
    else:
        if 'N' in request.GET:
            
            form        =   MYCASHFLOW.items.get(id=request.GET['N'])
            dict        =   model_to_dict(form)
            dict['id']  =   ''
            form=NewCashForm(dict)
            return render_to_response('cash.html', {'form': form},context_instance=RequestContext(request))
        
        elif 'delete' in request.GET:
        
            form        =   MYCASHFLOW.items.get(id=request.GET['delete'])
            form.delete()
            forms       =   MYCASHFLOW.items.filter(parent=request.GET['delete'])
            for item in forms:
                item.delete()
            return HttpResponseRedirect("/categ/")
        
        elif 'modify' in request.GET:
            
            instance        =   MYCASHFLOW.items.get(id=request.GET['modify'])
            intial_values   =   model_to_dict(instance)
            form            =   NewCashForm(intial_values)
            return render_to_response('cash.html', {'form': form},context_instance=RequestContext(request))
        
        msg='Please fill in the details of planned expense'
        return render_to_response('cash.html', ({'form': form,'errors':errors,'msg':msg}),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def events(request):
    event_list=[]
    calendar_items = MYCASHFLOW.items.raw("SELECT  id , direction , fdate ,  SUM(amount) as value FROM user_mycashflow GROUP BY fdate , direction ORDER by fdate")    
    for item in calendar_items:
        url='/report'+'?'+'today'+'='+item.fdate.isoformat()
        if item.direction == 'I':
            
            dict = { 'title' : 'Inflow   ' + str(item.value) + ' USD' , 'start':item.fdate.isoformat(), 'color':'#228B22' , 'url':url}
            event_list.append(dict)
        else:
            dict = { 'title' : 'Outflow   ' + str(item.value) + ' USD' , 'start':item.fdate.isoformat(), 'color':'#CD5C5C' , 'url':url}
            event_list.append(dict)
    
    json_data=jsonpickle.encode(event_list, unpicklable=False, make_refs=False)
    return HttpResponse(json_data, content_type='application/json')
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def calendar(request):
    return render_to_response('calendar.html',context_instance=RequestContext(request))
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
        default_values['corpid']='corpi'
        form=NewExpenseCategoryForm(default_values)
        if form.is_valid():
            newcateg = form.save()
            msg="Database Updated"
        else:
            msg=form.errors
        return render_to_response('cash.html',({'form': form,'errors':errors,'msg':msg}),context_instance=RequestContext(request))
    else:
        form=NewExpenseCategoryForm( )
#       return render_to_response('categ.html', {'form':form},context_instance=RequestContext(request))
        return render_to_response('addcateg.html', {'form':form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def launcher(request):
    return render_to_response("launcher.html", {'date':datetime.date.today()},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def contact(request):
    return render_to_response("contact.html",locals(),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/admin/')
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
@login_required(login_url='/home/')
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
    item={}      
    if request.method == 'POST':
        if ( request.POST['category_id'] != ""):
            row_data = MYCASHFLOW.items.filter(category_id=request.POST['category_id'],
                                               fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'])
        else:
            row_data = MYCASHFLOW.items.filter(fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'])
            
        for rows in row_data:
            if rows.direction == 'I':
                rows.amount = 1 * rows.amount    
            else:
                rows.amount = -1 * rows.amount    
            try:
                actual_entry=cashflow_actuals.items.get(cashflow_id=rows.id)
                item['id']=rows.id
                item['adate']=actual_entry.fdate
                item['category_id']=expense_categories.items.get(id=rows.category_id)
                
                item['amount']=rows.amount
                item['actualamount']=actual_entry.actualamount
                xitem = report_item(item['adate'],item.copy())
                dailyitems.append(xitem)

            except:
                item['id']=rows.id
                item['adate']=rows.fdate
                item['category_id']=expense_categories.items.get(id=rows.category_id)
                item['amount']=rows.amount
                xitem = report_item(item['adate'],item.copy())
                dailyitems.append(xitem)

        actuals_noref=cashflow_actuals.items.filter(cashflow_id__gte=90000)
        for noref_row in actuals_noref:
                    if rows.direction == 'I':
                        noref_row.amount = 1 * noref_row.amount    
                    else:
                        noref_row.amount = -1 * noref_row.amount    
                    item['id']=noref_row.cashflow_id
                    item['adate']=noref_row.fdate
                    item['category_id']=expense_categories.items.get(id=rows.category_id)
                    item['actualamount']=noref_row.actualamount
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
            items=MYCASHFLOW.items.filter(fdate=request.GET['today'])
            for item in items:
                row={'id':item.id,'date':item.fdate,'category_id':item.category_id,'amount':item.amount,'class':'line'}
                dailyitems.append(row)
            return render_to_response("dailyreport.html",{'dailyitems':dailyitems},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartdata(request):
    chart_data={}
    json_data= "none"
    row_data = MYCASHFLOW.items.raw("SELECT  id , category_id ,   SUM(amount) as value FROM user_mycashflow GROUP BY category_id ORDER by fdate")
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))
    
    for row in row_data:
        cell_data=[]
        cell_data.append({'v':expense_categories.items.get(id=row.category_id).__unicode__()})
        cell_data.append({'v':row.value})
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
    row_data = cashflow_actuals.items.raw("SELECT  id , category_id ,   SUM(amount) as value FROM user_cashflow_actuals GROUP BY category_id ORDER by fdate")
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))

    for row in row_data:
        cell_data=[]
        cell_data.append({'v':expense_categories.items.get(id=row.category_id).__unicode__()})
        cell_data.append({'v':row.value})
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
    row_data = MYCASHFLOW.items.raw("SELECT  id , direction ,   SUM(amount) as value FROM user_mycashflow GROUP BY direction ORDER by fdate")
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
        cell_data.append({'v':row.value})
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
    import calendar
    chart_data={}
    json_data= "none"
    row_data = MYCASHFLOW.items.raw("select  id  , sum(amount) as monthval , strftime('%m',fdate) as month from user_mycashflow group by strftime('%m',fdate)")
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'Month'}))
    chart_cols_data.append(({'type':'number','label':'Actual'}))
    chart_cols_data.append(({'type':'number','label':'Planned'}))
    for row in row_data:
        month = row.month
        month.strip('0')
        cell_data=[]
        cell_data.append({'v':calendar.month_name[int(month)]})
        cell_data.append({'v':row.monthval})
        cell_data.append({'v':'5000'})
        chart_rows_data.append({'c':cell_data})
    final_chart_data.append(chart_cols_data)
    final_chart_data.append(chart_rows_data)
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
         forecasted_entry=MYCASHFLOW.items.create(category=l_form.cleaned_data['category'],
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
         
     
     
     
     
     
     