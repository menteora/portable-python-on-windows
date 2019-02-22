from sqlalchemy import create_engine
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
        engine = create_engine(conn_str)
        self.connection = engine.connect()        
        
    def execute(self, query):
        self.result = self.connection.execute(query)

    def toDataframe(self):
        self.df = DataFrame(self.result.fetchall())
        return self.df