import xlwt

import sys, os, django
sys.path.append("/Users/mahtaakhyani/Documents/pycon") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pycon.settings")
django.setup()

from user.models import CustomUser

def export_users_xls():

    wb = xlwt.Workbook('userslist.xlsx')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['نام و نام خانوادگی', 'First name & Last name','کد ملی' ,'ایمیل',
     'شماره تلفن همراه', 'کد پستی', 'آدرس' , 'پرداخت شده' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = CustomUser.objects.all().values_list('name_fa', 'name_en','codemli',
     'email', 'phonenum' , 'postalcode' , 'address' , 'activate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save('userslist.xlsx')


export_users_xls()


