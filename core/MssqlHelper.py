
from sqlalchemy import create_engine

class MssqlHelper:        
    def executeQuery(user, password, host, database, query):
        conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
        engine = create_engine(conn_str)
        connection = engine.connect()
        return connection.execute(query)
