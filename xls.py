from calendar import weekday
from datetime import datetime

import openpyxl
from openpyxl import load_workbook


def writedata(sound,dust):
    now=datetime.now()
    current=now.strftime("%H:%M:%S")
    day=now.strftime("%A")
    wb= load_workbook(filename=r"C:\Users\Khoa\PycharmProjects\IOT\data.xlsx")
    ws=wb["Sheet1"]
    print(wb.sheetnames)
    lastrow=ws.max_row
    ws.cell(row=lastrow,column=1).value=day
    ws.cell(row=lastrow,column=2).value=current
    ws.cell(row=lastrow,column=3).value=sound
    ws.cell(row=lastrow,column=4).value=dust