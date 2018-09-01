import os
import json

class PathHelper:
    def getConfigPath():
        return PathHelper.__getDirectoryFromParent('configs')

    def getConfigJson(name):
        with open(os.path.join(PathHelper.getConfigPath(), name), 'r') as f:
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
