
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response is ok
if res.status_code == 200:
    # Access the content of the zip file
    zip_content = res.content
else:
    raise Exception("Error fetching the zip file from the API")
