import datetime
from datetime import timedelta, date
# Get the parameter [ daily , weekly , biweekly , monthly , quarterly , yearly. Return the list of
# dates based on the input parameters.
def get_occurances(frequency, start_date, timelimit=730):
    newdate= date.today()
    dates = []
    diff = timedelta(0)
    months=start_date.month
    year = start_date.year
    month_date = start_date.day
    next_date = start_date
    # Calculate dates based on the selection
    while ( diff.days < timelimit):
        if frequency == 'D':
            next_date = next_date + timedelta(days=1)
            newdate = next_date
        elif frequency == 'M':
            months = months + 1
            if months > 12:
                year = year + 1
                months=1
            if months==2 and ( start_date.day in [29,30,31]):
                month_date=28
            else:
                month_date= start_date.day
            if month_date == 31 and ( months in [4,6,9,11]) :
                month_date=30 #set to nearest
            newdate=date(day=month_date,month=months,year=year)
        elif frequency == 'B' : #"Biweekly"
            next_date = next_date + timedelta(weeks=2)
            newdate = next_date
        elif frequency == 'W':
            next_date = next_date + timedelta(days=7)
            newdate = next_date
        elif frequency == 'Q':
            l_month_date = l_months = 0
            next_date = next_date + timedelta(days=90)
            l_year = next_date.year
            l_months = next_date.month
            if next_date.day <= 15:
                l_month_date = 1
            elif next_date.day > 15:
                l_month_date = 1
                if l_months < 12 :
                    l_months =  l_months + 1
                else:
                    l_year = l_year + 1
                    l_months = 1
            newdate=date(day=l_month_date,month=l_months,year=l_year)
        elif frequency == 'Y':
            next_date = next_date + timedelta(days=365)
            newdate = next_date
        diff = newdate - start_date
        dates.append(newdate)
    return dates

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
class jdata:
    def __init__(self,total,page,records,rows):
        self.total=total
        self.page=page
        self.records=records
        self.rows=rows

class jevent:
   def __init__(self,events):
       self.events = events

import xlrd
#
class fileupload:

    log=[]
    sheets=[]
    errors =[]
    budget_table=[]
    categ_table=[]
    # read the file and create tables for bugget and categ columns
    def read_file(self,input_filename):
        try:
            workbook = xlrd.open_workbook(file_contents=input_filename.read())
            worksheets = workbook.sheet_names()
            if worksheets.__len__( ) > 2:
                self.log.append({'Error:':'Delete unwanted / addtional sheets'})
            else:
                sheets = workbook.sheet_names()
                count = 0
                for sheet in sheets:
                    if  sheet =='CATEG':
                        count = count + 1
                    elif sheet == 'BUDGET' :
                        count = count + 1
                if count < 2 :
                    self.errors.append({'Error:':'Not all sheets are present/ incorrectly named'})
        except(FileNotFoundError):
                self.log.append({'Error:': 'File Read Failed / File not found'})
    # read the file and create tables for bugget and categ columns
        budget_sheet = workbook.sheet_by_name('BUDGET')
        dict={}
        numrows  = budget_sheet.nrows - 1
        numcells = budget_sheet.ncols - 1
        curr_row = -1
        while curr_row < numrows:
            curr_row+=1
            row = budget_sheet.row(curr_row)
            curr_cell = -1
            while curr_cell < numcells:
                curr_cell+=1
                cell_type =  budget_sheet.cell_type(curr_row,curr_cell)
                cell_value = budget_sheet.cell_value(curr_row,curr_cell)
                if cell_type == xlrd.XL_CELL_DATE:
                    datetuple = xlrd.xldate_as_tuple(cell_value,workbook.datemode)
                    if datetuple[3:] == (0, 0, 0):
                        cell_value = datetime.date(datetuple[0], datetuple[1], datetuple[2])
                dict[curr_cell]=cell_value
                if curr_cell == 17:
                    self.budget_table.append(dict.copy())
                    dict={}
    # read the file and create tables for bugget and categ columns
        categ_sheet = workbook.sheet_by_name('CATEG')
        numrows  = categ_sheet.nrows - 1
        numcells = categ_sheet.ncols - 1
        curr_row = -1
        while curr_row < numrows:
            curr_row+=1
            row = categ_sheet.row(curr_row)
            curr_cell = -1
            while curr_cell < numcells:
                curr_cell+=1
                cell_type =  categ_sheet.cell_type(curr_row,curr_cell)
                cell_value = categ_sheet.cell_value(curr_row,curr_cell)
                dict={}
                dict[curr_cell]=cell_value
                self.categ_table.append(dict)
    def get_categ_table(self):
        return  self.categ_table
    def get_budget_table(self):
        return  self.budget_table

    # if ecnt == 0:
    #                 #Directon,category,frequency,fdate,amount,currency,recipient name street city zipcode region paymethod telephone email fax notes1  notes2 notes3
    #                     cnt = 0
    #                     for eachcashflow in budget_table:
    #                     #First record is header , not required
    #                         cnt = cnt + 1
    #                         if cnt == 1:
    #                             continue
    #                         direction=eachcashflow[0]
    #                         category=eachcashflow[1]
    #                         frequency=eachcashflow[2]
    #                         fdate=eachcashflow[3]
    #                         amount=eachcashflow[4]
    #                         currency=eachcashflow[5]
    #                         recipient=eachcashflow[6]
    #                         name=eachcashflow[7]
    #                         street=eachcashflow[8]
    #                         city=eachcashflow[9]
    #                         zipcode=eachcashflow[10]
    #                         region=eachcashflow[11]
    #                         paymethod=eachcashflow[12]
    #                         telephone=eachcashflow[13]
    #                         email=eachcashflow[14]
    #                         fax=eachcashflow[15]
    #                         notes1=eachcashflow[16]
    #                         notes2=eachcashflow[17]
    #                         notes3=eachcashflow[18]
    #
    #                         dict={}
    #                         dict['user']          = request.user.get_short_name()
    #                         dict['corpid']        = request.user.get_corpid()
    #                         dict['direction']     = direction[1].upper()
    #                         dict['category']      = category.strip().upper()
    #                         dict['frequency']     = frequency[1].strip().upper()
    #                         dict['fdate']         = fdate
    #                         dict['amount']        = amount
    #                         dict['currency']      = request.user.get_currency()
    #                         dict['recipient']     = recipient.strip().upper()
    #                         dict['name']          = name.strip().upper()
    #                         dict['street']        = street.strip().upper()
    #                         dict['city']          = city.strip().upper()
    #                         dict['zipcode']       = zipcode.strip().upper()
    #                         dict['region']        = region.strip().upper()
    #                         dict['paymethod']    = paymethod[1].strip().upper()
    #                         dict['telephone']     = telephone.strip().upper()
    #                         dict['email']         = email.strip().upper()
    #                         dict['fax']           = fax.strip().upper()
    #                         dict['notes1']        = notes1.strip().upper()
    #                         dict['notes2']        = notes2.strip().upper()
    #                         dict['notes3']        = notes3.strip().upper()
    #
    #                         cash_instance = MYCASHFLOW()
    #                         try:
    #                             cash_instance.save()
    #                             result=cash_instance.id
    #                         except(Exception):
    #                             result = None
    #                         if result == '' :
    #                             ecnt = ecnt + 1
    #                         else:
    #                             scnt = scnt + 1
    #                         status={}
    #                         error = 'Total' + str(cnt-1) + '  ' + 'Success' + str(scnt) + ' ' + 'Error' + ' ' + str(ecnt)
    #                         status={'cash upload upload':error}
    #                 return HttpResponse(error)
    #             else:
    #                 return HttpResponse(fileobj.errors)