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
# logging.basicConfig(filename=parentDir + '\logs\executor.log',level=logging.DEBUG)
log = logger.setup('executor', parentDir)
log.debug('This message should go to the log file')
log.info('So should this')
log.warning('And this, too')

with open(fileDir + '\executor.config.json', 'r') as f:
    config = json.load(f)

main_task = config['MAIN_TASK']['EXEC'] 
print(main_task)
return_code = subprocess.run(main_task).returncode
print(return_code)


input("Press enter to continue...")

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