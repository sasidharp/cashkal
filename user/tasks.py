__author__ = 'root'
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from celery import task

@task()
def add(x,y):
    return x + y

@task()
def send_complaint_async( ):
    email = 'sasidharp@gmail.com'
    send_mail('We have have received your request',
              "Please give us 2-3 days to respond to your request \n  Thank you \n Cashal Customer Support Team \n 1-800-CASHCAL",
              settings.DEFAULT_FROM_EMAIL,[email,])

@task()
def send_weekly_async( ):
    email_sub = 'Your upcoming Cash flows for the period <from> (Monday) <to> (Sunday)'
    email_body=[]

    email_bodyline = 'Dear <User> (take the value in First Name field)'
    email_body.append(email_bodyline)

    email_bodyline = 'Here is a snapshot of the cash flows planned for next week'
    email_body.append(email_bodyline)

    openitems = MYCASHFLOW.items.filter(corpid='12').filter(converted='')
    if openitems:
        for item in openitems:
            email_bodyline = 'Table lines'
            email_body.append(email_bodyline)

    else:
        email_bodyline = 'No cashflows planned for upcoming week'
        email_body.append(email_bodyline)

    email_bodyline = 'Cheers \n Team CashKal'
    email_body.append(email_bodyline)

    send_mail(email_sub,
              "Please give us 2-3 days to respond to your request \n  Thank you \n Cashal Customer Support Team \n 1-800-CASHCAL",
              settings.DEFAULT_FROM_EMAIL,['sasidharp@gmail.com',])

def reminder_run():
    #Get all the users in the database
    users = MyUser.items.all()
    #Iterate through the users
    for user in users:
        print('start of the run')
        bodystring=''
        body=[]
        if user.get_TypeofOrg() == 1 :
            cashitems = MYCASHFLOW.items.filter(user=user.get_short_name())
        else:
            cashitems = MYCASHFLOW.items.filter(corpid=user.get_corpid())

        if cashitems:
            body.append("""Dear '{name}'""".format(name=user.get_short_name()))
            body.append("Here is a snapshot of the cash flows planned for next week")
            for items in cashitems:
                print('item')
                body.append('<table style="width:100%"><tr><td>Jill</td><td>Smith</td><td>50</td></tr><tr><td>Eve</td><td>Jackson</td><td>94</td></tr></table>')
            body.append("Cheers")
            body.append("Team Cashkal")
            bodystring = '<br>'.join(body)
            print('sending email to',user.get_short_name())
            send_mail("""Your upcoming Cash flows for the period '{begin}' to '{end}'""".format(begin=datetime.date.today() ,end=datetime.date.today()),
                      bodystring,
                      settings.DEFAULT_FROM_EMAIL,[user.get_short_name(),],html_message=bodystring)


# <!DOCTYPE html>
# <html>
#
# <head>
# <style>
# table, th, td {
#     border: 1px solid black;
#     border-collapse: collapse;
# }
# th, td {
#     padding: 5px;
#     text-align: left;
# }
# </style>
# </head>
#
# <body>
#
# <table style="width:100%">
#   <caption>Monthly savings</caption>
#   <tr>
#     <th>Month</th>
#     <th>Savings</th>
#   </tr>
#   <tr>
#     <td>January</td>
#     <td>$100</td>
#   </tr>
#   <tr>
#     <td>February</td>
#     <td>$50</td>
#   </tr>
# </table>
#
# </body>
# </html>
