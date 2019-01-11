import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper

class MsExcelExtractor(DataExtractor):

    def connect(self):
        file = self.config_json['source']['file']
        self.df = pd.read_excel(file, encoding='utf-8')
        
    def execute(self):
        raise ValueError('Not necessary at the moment!')

    def toDataframe(self):
        return self.df