from django.shortcuts import render,render_to_response , RequestContext
from .forms import *
from django.http import HttpResponse
from .models import expense_categories
from .models import MYCASHFLOW,cashflow_actuals,contact
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
from .BusinessLogic import jdata ,get_occurances
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def logout1(request):
    logout(request)
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))
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

        form=UserCreationForm(default_values)
        if form.is_valid():
            form.save()
            # return render_to_response('signup.html',({'form':form},{'msg':'Registered'}),context_instance=RequestContext(request))
            user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            if user:
                login(request, user)
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
    if 'L' in request.GET :
        raw_sql="""SELECT * FROM user_mycashflow where fdate <= '{today_date}' and "user" = '{username}'""".format(today_date=datetime.date.today(),username=request.user)
    else:
        raw_sql="""SELECT * FROM user_mycashflow where "user" = '{username}'""".format(today_date=datetime.date.today(),username=request.user)

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
    raw_sql="""SELECT * FROM user_cashflow_actuals where "user" = '{username}'""".format(username=request.user)
    row_list = cashflow_actuals.items.raw(raw_sql)
#   append them into row
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
def cashactuals(request):
    
    msg=''
    errors={} 
    formdate={}
    default_values={}
    
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

        elif 'delete' in request.GET:
            form=cashflow_actuals.items.get(id=request.GET['delete'])
            form.delete()
            return HttpResponseRedirect("/categ/")
        elif 'modify' in request.GET:
            instance=cashflow_actuals.items.get(id=request.GET['modify'])
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
        default_values['user']        = request.user
        default_values['corpid']      = request.user.get_corpid()
        default_values['parent']      ='P'
        default_values['currency']    = request.user.get_currency()
       
        form = NewCashForm(default_values)
        
        if form.is_valid():
                id=form.save()
                msg='Entry Saved'
                if form.cleaned_data['frequency'] != 'S':
                    create_forecasted_entries(form,id,request)
                form = NewCashForm()
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

    return render_to_response('cash.html', ({'form': form}),context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def events(request):
    from django.db import connection
    calendar_final=[]
    event_list=[]
    raw_stmt ="""select fdate  ,  direction , sum(amount) as value  from user_mycashflow where "user" = '{user_name}'  group by fdate ,direction order by fdate , direction""".format(user_name=request.user)
    cursor = connection.cursor()
    cursor.execute(raw_stmt)
    calendar_items = cursor.fetchall()
    for item in calendar_items:
        url='/report'+'?'+'today'+'='+item[0].isoformat()
        if item[1] == 'I':
            
            dict = { 'title' : 'Rcvd         ' + str(item[2]) + request.user.get_currency() , 'start':item[0].isoformat(), 'color':'#228B22' , 'url':url}
            event_list.append(dict)
        else:
            dict = { 'title' : 'Not Rcvd   ' + str(item[2]) + request.user.get_currency() , 'start':item[0].isoformat(), 'color':'#CD5C5C' , 'url':url}
            event_list.append(dict)
    
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
        form = ModalActualForm(request.POST)
        if form.is_valid():
            form.save()
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
         myuser.search1_tag=request.GET['calop']
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
    return render_to_response('calendar.html',{'user_option':'W'},context_instance=RequestContext(request))
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
        else:
            msg='Invalid categ'
        return render_to_response('addcateg.html',({'form': form,'msg':msg}),context_instance=RequestContext(request))
    else:
        form=NewExpenseCategoryForm( )
        return render_to_response('addcateg.html', {'form':form},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
@login_required(login_url='/home/')
def launcher(request):
    form = ModalActualForm()
    return render_to_response("launcher.html", {'date':datetime.date.today(),'form':form},context_instance=RequestContext(request))

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
def contact(request):
    form = NewContactForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return render_to_response("contact.html",{'form':form},context_instance=RequestContext(request))
    else:
        return render_to_response("contact.html",{'form':form},context_instance=RequestContext(request))

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
    item={}      
    if request.method == 'POST':
        if ( request.POST['category_id'] != ""):
            row_data = MYCASHFLOW.items.filter(category_id=request.POST['category_id'],
                                               fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'],
                                               user=request.user)
        else:
            row_data = MYCASHFLOW.items.filter(fdate__gte=request.POST['start_date'],
                                               fdate__lte=request.POST['end_date'],
                                               user=request.user)
            
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
                    if noref_row.direction == 'I':
                        noref_row.amount = 1 * noref_row.amount    
                    else:
                        noref_row.amount = -1 * noref_row.amount    
                    item['id']=noref_row.cashflow_id
                    item['adate']=noref_row.fdate
                    item['category_id']=expense_categories.items.get(id=noref_row.category_id)
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
            items=MYCASHFLOW.items.filter(fdate=request.GET['today'],
                                          user=request.user)
            for item in items:
                row={'id':item.id,'date':item.fdate,'category_id':expense_categories.items.get(id=item.category_id),'amount':item.amount,'class':'line'}
                dailyitems.append(row)
            return render_to_response("dailyreport.html",{'dailyitems':dailyitems},context_instance=RequestContext(request))
#**********************************************************************************************#
#                               Create your views here.                                        #
#**********************************************************************************************#
def overallchartdata(request):
    chart_data={}
    json_data= "none"
    raw_stmt="""SELECT  DISTINCT ON (category_id) category_id  , id  , (select SUM(amount) from user_mycashflow where category_id = a.category_id and "user" = '{user}') as value from user_mycashflow
                    as a where "user" = '{user}' group by  category_id , id order by category_id""".format(user=request.user)
    row_data = MYCASHFLOW.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))
    
    for row in row_data:
        cell_data=[]
        cell_data.append({'v':expense_categories.items.get(id=row.category_id).__unicode__()})
        cell_data.append({'v':int(row.value)})
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
    raw_stmt="""SELECT  DISTINCT ON (category_id) category_id  , id  , (select SUM(actualamount) from user_cashflow_actuals where category_id = a.category_id and "user" = '{user}') as value from user_cashflow_actuals
                    as a where "user" = '{user}' group by  category_id , id order by category_id""".format(user=request.user)
    row_data = cashflow_actuals.items.raw(raw_stmt)
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'category'}))
    chart_cols_data.append(({'type':'number','label':'amount'}))

    for row in row_data:
        cell_data=[]
        cell_data.append({'v':expense_categories.items.get(id=row.category_id).__unicode__()})
        cell_data.append({'v':int(row.value)})
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
    cursor = connection.cursor()
    cursor.execute("""select extract(month from fdate) as month,extract(year from fdate) as yyyy,sum(amount) as monthval from user_mycashflow group by 1,2""")
    row_data = cursor.fetchall()
    final_chart_data=[]
    chart_rows_data=[]
    chart_cols_data=[]
    chart_cols_data.append(({'type':'string','label':'Month'}))
    chart_cols_data.append(({'type':'number','label':'Actual'}))
    chart_cols_data.append(({'type':'number','label':'Planned'}))
    for row in row_data:
        month = row[0]
        cell_data=[]
        cell_data.append({'v':calendar.month_name[int(month)]})
        cell_data.append({'v':int(row[2])})
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
         
     
     
     
     
     
     
