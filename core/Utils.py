import os
import json
import getpass
import socket
from pathlib import Path

class PathHelper:
    def getConfigPath():
        return PathHelper.__getDirectoryFromParent('configs')

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
        return PathHelper.__getDirectoryFromParent('scripts')

    def getLogsPath():
        return PathHelper.__getDirectoryFromParent('logs')

    def getCorePath():
        return PathHelper.__getCurrentDirectory() 

    def __getCurrentDirectory():
        return os.path.dirname(os.path.abspath(__file__))
    
    def __getParentDirectory():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __getDirectoryFromParent(folder):
        return os.path.join(PathHelper.__getParentDirectory(), folder)
