import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper

class MsExcelExtractor(DataExtractor):

    def connect(self):
        file = self.config_json['source']['file']
        sheet_name = self.config_json['source']['sheet_name'] if 'sheet_name' in self.config_json['source'] else 0
        # print('************************************************* {}'.format(sheet_name))
        self.df = pd.read_excel(file, encoding='utf-8', sheet_name = sheet_name)
        
    def execute(self):
        raise ValueError('Not necessary at the moment!')

    def toDataframe(self):
        return self.df