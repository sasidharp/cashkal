__author__ = 'sapurana'

list=[]

list.append(('A',100))
list.append(('A',100))
list.append(('A',100))
list.append(('A',100))
list.append(('B',400))
list.append(('B',100))
list.append(('B',100))
list.append(('B',100))
list.append(('X',104))
list.append(('X',104))
list.append(('X',104))
list.append(('X',140))
list.append(('Y',104))
list.append(('Y',104))
list.append(('Y',140))

tmpvalue='A'
amount = 0
cnt = 0
final_record = list.__len__()
for item in list:
    cnt = cnt + 1
    if item[0] != tmpvalue:
         print('Subtotal'+tmpvalue+str(amount))
         amount=0
         tmpvalue = item[0]
    amount = amount + item[1]
    print(item[0])
    if cnt == final_record:
               print('Subtotal'+tmpvalue+str(amount))
