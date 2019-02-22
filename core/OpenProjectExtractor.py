import pandas as pd
from DataExtractor import DataExtractor
from Utils import PathHelper
import requests
import json
from pandas.io.json import json_normalize

class OpenProjectExtractor(DataExtractor):

    def connect(self):
        pass

    def execute(self, url):
        response = requests.get(url, auth=('apikey', self.config_json['authentication']['api_key']))
        response.encoding = 'utf-8'
        # self.result = json.loads(response.text)
        self.result = response.json()
        self.original_result = self.result

    def toDataframe(self):
        self.df = pd.DataFrame.from_dict(json_normalize(self.result), orient='columns')
        # self.df = pd.io.json.json_normalize(self.result)
        return self.df
        # self.df = pd.read_json(self.result)
        # return self.df

    def getCurrentJson(self):
        return self.result

    def setCustomJson(self, json):
        self.result = json

    def setOriginalJson(self):
        self.result = self.original_result





