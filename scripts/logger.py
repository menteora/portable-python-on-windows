import sys
import logging

def setup(name, dir):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(filename=dir + '\logs\executor.log', mode='a')
    handler.setFormatter(formatter)
    #screen_handler = logging.StreamHandler(stream=sys.stdout)
    #screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    #logger.addHandler(screen_handler)
    return logger