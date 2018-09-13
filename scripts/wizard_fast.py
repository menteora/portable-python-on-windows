#https://www.blog.pythonlibrary.org/2012/07/12/wxpython-how-to-create-a-generic-wizard/
#http://www.blog.pythonlibrary.org/2011/01/27/wxpython-a-wizard-tutorial/
#http://www.blog.pythonlibrary.org/2010/03/26/creating-a-simple-photo-viewer-with-wxpython/
#https://stackoverflow.com/questions/21766289/how-do-i-pass-information-between-pages-of-a-wxpython-pywizardpage-wizard
#https://www.blog.pythonlibrary.org/2013/09/04/wxpython-how-to-update-a-progress-bar-from-a-thread/

import os
import wx
import wx.adv as wiz
import sys
import json
from pandas import DataFrame
import pandas as pd
from threading import Thread
from wx.lib.pubsub import pub
import locale
from locale import atof
import datetime
#from babel.numbers import format_number, format_decimal, format_percent
#from wx.adv import Animation, AnimationCtrl
# Append core folder
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'core'))
# Import core Classes
from Utils import PathHelper
from Utils import Singleton
from MssqlHelper import MssqlHelper

'''
def convert_currency(val):
    print(val)
    new_val = format_decimal(val, locale='it_IT')
    print(new_val)
    return float(new_val)
'''

database = MssqlHelper()
engine = database.getEngine()
df = pd.read_excel(PathHelper.getCustomConfigPath('excel_fornitore.xlsx'))[['Codice', 'Prezzo']]
df.to_sql('ListinoZebra', con=engine, if_exists='replace')
#Get results from Navision
result = engine.execute("SELECT * FROM MIGLISTINO07_ALLCROSS_LISTINOZEBRA")
df = DataFrame(result.fetchall())
df.columns = result.keys()

writer = pd.ExcelWriter('incrocio_zebra_crossnav.xlsx', 
                engine='xlsxwriter', 
                datetime_format='dd/mm/yyyy',
                date_format='dd/mm/yyyy')
sheetname = 'report'
#df['Quantita Minima'].apply(convert_currency)
#df['Prezzo Unitario'] = [str(val).replace('.', ',') for val in df['Prezzo Unitario']]
df['Prezzo Unitario'] = df['Prezzo Unitario'].astype(str).astype(float)
df['Quantita Minima'] = df['Quantita Minima'].astype(str).astype(float)
df.to_excel(writer, 
            index=False, 
            sheet_name=sheetname)
workbook = writer.book
worksheet = writer.sheets[sheetname]
# Add a number format for cells with money.
money_fmt = workbook.add_format({'num_format': '0.00', 'bold': True})
# Monthly columns
worksheet.set_column('F:F', None, money_fmt)
worksheet.set_column('E:E', None, money_fmt)
#Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
for i, col in enumerate(df.columns):
    # find length of column i
    column_len = df[col].astype(str).str.len().max()
    # Setting the length if the column header is larger
    # than the max column value length
    column_len = max(column_len, len(col)) + 2
    # set the column length
    worksheet.set_column(i, i, column_len)

writer.save()

