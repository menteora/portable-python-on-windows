from sqlalchemy import create_engine
from pandas import DataFrame
import pandas as pd
import json
import os

#https://www.dataquest.io/blog/excel-and-pandas/
fileDir = os.path.dirname(os.path.abspath(__file__))

with open(fileDir + '\mssql_extractor.config.json', 'r') as f:
    config = json.load(f)

user = config['authentication']['user']
password = config['authentication']['password']
host = config['authentication']['host']
database = config['authentication']['database']
query = config['authentication']['query']
filename = config['excel']['file_name']

conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
engine = create_engine(conn_str)
connection = engine.connect()
result = connection.execute(query)

df = DataFrame(result.fetchall())
df.columns = result.keys()

writer = pd.ExcelWriter(filename, engine='xlsxwriter')

#writer = StyleFrame.ExcelWriter('example.xlsx')
#sf = StyleFrame(df)
#sf.to_excel(excel_writer=writer)

df.to_excel(writer, index=False, sheet_name='report')

#Indicate workbook and worksheet for formatting
workbook = writer.book
worksheet = writer.sheets['report']

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