
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from myapp.models import UploadedFile  # Adjust import based on your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Create a File-like object from the response content
if response.status_code == 200:
    # Save the zip file to the UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_file.zip', ContentFile(response.content), save=True)
else:
    print("Failed to fetch the file: ", response.status_code)
