import os
import json

fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
with open(fileDir + '\executor.config.json', 'r') as f:
    config = json.load(f)

secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'
print(secret_key)
print(ci_hook_url)

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
