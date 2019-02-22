from Utils import PathHelper
import pandas as pd

class CsvTransformer():

    def __init__(self, file_path):
        if isinstance(file_path, list):
            dfs = [pd.read_csv(f, encoding='utf-8')
                for f in file_path]
            self.df = pd.concat(dfs).sort_index()
        else:
            self.df = pd.read_csv(file_path, encoding='utf-8')

    def filterColumn(self, columns = []):
        self.df = self.df[columns]

    def write(self, file_path, df=None):
        if df is None:
            self.df.to_csv(file_path, sep=',', encoding='utf-8', index=None)
        else:
            df.to_csv(file_path, sep=',', encoding='utf-8', index=None)

    def appendRow(self, row):
        self.df.loc[len(self.df)] = row

    def addColumnWithFixedValue(self, name, value):
        self.df[name] = value

    def getDataframe(self):
        return self.df

    def mergeDataframes(self, df, left_on, right_on , suffixes=(False, False)):
        self.df.merge(df, left_on=left_on, right_on=right_on, suffixes=suffixes)

    def replace(to_replace, value, regex):
        self.df.replace(to_replace=to_replace, value=value, regex=regex)