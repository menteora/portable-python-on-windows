from sqlalchemy import create_engine
from pandas import DataFrame
import pandas as pd

#https://www.dataquest.io/blog/excel-and-pandas/
fileDir = os.path.dirname(os.path.abspath(__file__))

with open(fileDir + '\mssql_extractor.config.json', 'r') as f:
    config = json.load(f)

user = config['authentication']['user']
password = config['authentication']['password']
host = config['authentication']['host']
database = config['authentication']['database']
query = config['authentication']['query']

conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
engine = create_engine(conn_str)
connection = engine.connect()
result = connection.execute(query)

df = DataFrame(result.fetchall())
df.columns = result.keys()

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

df.to_excel(writer, index=False, sheet_name='report')
writer.save()