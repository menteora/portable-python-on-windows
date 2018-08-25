import json
import requests, zipfile, io

repository_url = 'https://api.github.com/repos/menteora/isakk/releases/latest'
response = requests.get(repository_url)
json_data = json.loads(response.text)

zip_file_url = json_data['assets'][0]['browser_download_url']

r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()