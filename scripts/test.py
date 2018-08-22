import os

fileDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(fileDir) 
newPath = os.path.join(parentDir, 'logs') 
files = os.listdir(newPath)
print(files)


for index, curr_file in enumerate(files):
    files[index] = newPath + "\\" + curr_file

print(files)