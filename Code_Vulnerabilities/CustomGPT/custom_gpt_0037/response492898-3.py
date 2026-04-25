
import requests
from django.core.files.base import ContentFile
from .models import UploadedFile  # Adjust import according to your project structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    zip_content = res.content
    # Save the zip file to the model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_content))
    uploaded_file.save()
else:
    print("Failed to retrieve zip file from API")
