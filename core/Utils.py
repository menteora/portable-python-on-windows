import os
import json
import getpass
import socket
from pathlib import Path

class PathHelper:
    def getConfigPath():
        return PathHelper.__getDirectoryFromParentPath('configs')

    def getConfigJson(name):
        config_file = os.path.join(PathHelper.getConfigPath(), name + ".config.json")
        config = False
        if Path(config_file).exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
        return config

    def getCustomConfigPath(name):
        config_file = os.path.join(PathHelper.getConfigPath(), name)
        return config_file

    def getUserConfigJson():
        user_file = os.path.join(PathHelper.getConfigPath(), getpass.getuser() + ".config.json")
        config = False
        if Path(user_file).exists():
            with open(user_file, 'r') as f:
                config = json.load(f)
        return config

    def getHostConfigJson():
        host_file = os.path.join(PathHelper.getConfigPath(), socket.gethostname() + ".config.json")
        config = False
        if Path(host_file).exists():
            with open(host_file, 'r') as f:
                config = json.load(f)
        return config

    def getScriptsPath():
        return PathHelper.__getDirectoryFromParentPath('scripts')

    def getLogsPath():
        return PathHelper.__getDirectoryFromParentPath('logs')

    def getCorePath():
        return PathHelper.__getCurrentDirectoryPath() 

    def __getCurrentDirectoryPath():
        return os.path.dirname(os.path.abspath(__file__))
    
    def __getParentDirectoryPath():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __getDirectoryFromParentPath(folder):
        return os.path.join(PathHelper.__getParentDirectoryPath(), folder)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]