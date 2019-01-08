import os
import json
import getpass
import socket
import time
from pathlib import Path


class PathHelper:
    def getConfigPath(name=''):
        if name == '':
            return PathHelper.__getDirectoryFromAppsPath('configs')
        else:
            return os.path.join(
            PathHelper.getConfigPath(), name)
            
    def getConfigJson(name):
        config_file = os.path.join(
            PathHelper.getConfigPath(), name + ".config.json")
        config = False
        if Path(config_file).exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
        return config

    def getCustomFileAsset(name):
        config_file = os.path.join(PathHelper.getAssetsPath(), name)
        return config_file

    def getCustomBinFile(relative_directory, name):
        config_file = os.path.join(PathHelper.getBinPath(), relative_directory, name)
        return config_file

    def getCustomLogFile(name):
        config_file = os.path.join(PathHelper.getLogsPath(), name)
        return config_file

    def getCustomLogFileTimeStamp(name):
        config_file = os.path.join(PathHelper.getLogsPath(), time.strftime("%Y%m%d-%H%M%S") + "_" + name)
        return config_file

    def getUserConfigJson():
        user_file = os.path.join(
            PathHelper.getConfigPath(), getpass.getuser() + ".config.json")
        config = False
        if Path(user_file).exists():
            with open(user_file, 'r') as f:
                config = json.load(f)
        return config

    def getHostConfigJson():
        host_file = os.path.join(
            PathHelper.getConfigPath(), socket.gethostname() + ".config.json")
        config = False
        if Path(host_file).exists():
            with open(host_file, 'r') as f:
                config = json.load(f)
        return config

    def getScriptsPath():
        return PathHelper.__getDirectoryFromAppsPath('scripts')

    def getLogsPath():
        return PathHelper.__getDirectoryFromAppsPath('logs')

    def getAssetsPath():
        return PathHelper.__getDirectoryFromAppsPath('assets')

    def getBinPath():
        return PathHelper.__getDirectoryFromAppsPath('bin')

    def getCorePath():
        return os.path.dirname(os.path.abspath(__file__))

    def __getAppsDirectoryPath():
        return os.getcwd()

    def __getDirectoryFromAppsPath(folder):
        return os.path.join(PathHelper.__getAppsDirectoryPath(), folder)


'''
    def __getCurrentDirectoryPath():
        return os.path.dirname(os.path.abspath(__file__))
    def __getParentDirectoryPath():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def __getDirectoryFromParentPath(folder):
        return os.path.join(PathHelper.__getParentDirectoryPath(), folder)
'''


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
