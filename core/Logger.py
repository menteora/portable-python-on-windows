import logging
from Utils import Singleton
from Utils import PathHelper

'''
class Logger:
    def setup(name, dir):
        formatter = logging.Formatter(
                        fmt='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler(
                        filename=dir + '\logs\executor.txt', mode='a')
        handler.setFormatter(formatter)
        # screen_handler = logging.StreamHandler(stream=sys.stdout)
        # screen_handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        # logger.addHandler(screen_handler)
        return logger
'''


class Logger(metaclass=Singleton):
    def __init__(self):
        formatter = logging.Formatter(
                        fmt='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
        handler = logging.FileHandler(
                        filename=PathHelper.getCustomLogFile('app.log'),
                        mode='a')
        handler.setFormatter(formatter)
        # screen_handler = logging.StreamHandler(stream=sys.stdout)
        # screen_handler.setFormatter(formatter)
        self.logger = logging.getLogger('prova')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    def getLogger(self):
        return self.logger

    def setLogger(self, file_name):
        pass
