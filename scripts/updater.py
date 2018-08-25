import json
import requests 
import zipfile 
import io
import shutil
import os

def get_program_folder():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get lastest release from github
repository_url = 'https://api.github.com/repos/menteora/isakk/releases/latest'
response = requests.get(repository_url)
json_data = json.loads(response.text)

zip_file_url = json_data['assets'][0]['browser_download_url']
tag_name = json_data['tag_name']

# Unzip repository
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

current_dir = get_program_folder()
print(current_dir)
update_dir = os.path.join(current_dir, 'isakk')
print(update_dir)

update_files = os.listdir(update_dir)

for f in files:
    shutil.move(update_files+f, update_dir)