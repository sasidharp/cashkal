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
       