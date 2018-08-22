import os
import json
import subprocess
import importlib.util

def import_library(dir, name):
    spec = importlib.util.spec_from_file_location(name, fileDir + "/" + name +".py")
    library = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(library)
    return library

fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir)

logger = import_library(fileDir, "logger")

log = logger.setup('executor', parentDir)

with open(fileDir + '\executor.config.json', 'r') as f:
    config = json.load(f)

current_task = "MAIN_TASK"

while current_task != "END_TASK":
    main_task = config[current_task]['EXEC']
    log.info(main_task)
    return_code = subprocess.run(main_task).returncode
    log.debug(return_code)
    if return_code == 0:
        current_task = config[current_task]['SUCCESS'] 
    else:
        current_task = config[current_task]['FAILURE'] 


#input("Press enter to continue...")

'''
absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
print(fileDir)
parentDir = os.path.dirname(fileDir)                   # Directory of the Module directory
print(parentDir)
newPath = os.path.join(fileDir, 'executorconfig')   # Get the directory for StringFunctions
print(newPath)
'''