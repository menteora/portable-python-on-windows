import os
import json
import subprocess
import logging

fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
parentDir = os.path.dirname(fileDir)

logging.basicConfig(filename=parentDir + '\logs\executor.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

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
