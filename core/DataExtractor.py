from abc import ABC, abstractmethod
from Utils import PathHelper

class DataExtractor(ABC):

    def __init__(self, config={}):
        self.config_json = self.getConfig(config)
        self.connect()

    def getConfig(self, config={}):
        if config == {}:
            config_name = self.__class__.__name__
            return PathHelper.getConfigJson(config_name)
        else:
            return config

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def toDataframe(self):
        pass

    def toCsv(self, path):
        self.df.to_csv(path, sep=',', encoding='utf-8', index=None)