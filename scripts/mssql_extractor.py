from sqlalchemy import create_engine
conn_str = r'mssql+pymssql://(local)\SQLEXPRESS/myDb'
engine = create_engine(conn_str)
connection = engine.connect()
result = connection.execute("SELECT SYSTEM_USER AS me")
row = result.fetchone()
print(row['me'])