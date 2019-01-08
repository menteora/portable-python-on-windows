from abc import ABC, abstractmethod
from Utils import PathHelper

class DataExtractor(ABC):

    def getConfig(self, config={}):
        if config == {}:
            config_name = self.__class__.__name__
            return PathHelper.getConfigJson(config_name)
        else:
            config_name = config
            return PathHelper.getConfigJson(config_name)

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def toDataframe(self):
        pass