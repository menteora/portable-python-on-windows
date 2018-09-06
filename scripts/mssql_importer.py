from sqlalchemy import create_engine
from pandas import DataFrame
import pandas as pd
import json
import os
import sys
# Append core folder
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'core'))
# Import core Classes
from Utils import PathHelper

#https://trendct.org/2016/08/05/real-world-data-cleanup-with-python-and-pandas/
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
sheetname = config['excel']['sheet_name']

conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
engine = create_engine(conn_str)
df = pd.read_excel(PathHelper.getCustomConfigPath('excel_fornitore.xlsx'))[['Codice', 'Prezzo']]
print(df)
df.to_sql('ListinoZebra', con=engine, if_exists='replace')
print(engine.execute("SELECT * FROM ListinoZebra").fetchall())

