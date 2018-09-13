# StandarClass
from sqlalchemy import create_engine

# Core folders
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'core'))
# Core Classes
from Utils import PathHelper

class MssqlHelper:
    def __init__(self, config={}):
        if config == {}:
            config_name = self.__class__.__name__
            self.config_json = PathHelper.getConfigJson(config_name)
        else:
            config_name = config
            self.config_json = PathHelper.getConfigJson(config_name)
            
        user = self.config_json['authentication']['user']
        password = self.config_json['authentication']['password']
        host = self.config_json['authentication']['host']
        database = self.config_json['authentication']['database']
        conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
        self.config_engine = create_engine(conn_str)

    def getEngine(self):
        return self.config_engine

    def executeQuery(self, query):
        connection = self.config_engine.connect()
        return connection.execute(query)
