
import requests
from django.core.files import File
from django.core.files.base import ContentFile
from .models import UploadedFile

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if response.status_code == 200:
    # Create a ContentFile with the response content
    zip_file_content = ContentFile(response.content)

    # Create a new UploadedFile instance
    my_uploaded_file = UploadedFile(file=zip_file_content)

    # Save the instance to the database
    my_uploaded_file.save()
else:
    print("Failed to retrieve the zip file")
