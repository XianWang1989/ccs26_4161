
import requests

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    zip_content = res.content
else:
    raise Exception("Failed to download zip file.")
