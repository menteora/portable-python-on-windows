import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper

class MssqlExtractor(DataExtractor):

    def connect(self):
        user = self.config_json['authentication']['user']
        password = self.config_json['authentication']['password']
        host = self.config_json['authentication']['host']
        database = self.config_json['authentication']['database']
        conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
        self.engine = create_engine(conn_str)
        connection = self.engine.connect()        
        
    def execute(self, query):
        self.result = connection.execute(query)

    def toDataframe(self):
        df = DataFrame(self.result.fetchall())
        return df