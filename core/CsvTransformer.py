from Utils import PathHelper
import pandas as pd

class CsvTransformer():

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, encoding='utf-8')

    def filterColumn(self, columns = []):
        self.df = self.df[columns]

    def write(self, file_path):
        self.df.to_csv(file_path, sep=',', encoding='utf-8', index=None)