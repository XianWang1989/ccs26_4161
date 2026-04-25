
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

def save_zip_from_api():
    # Make the API call
    response = requests.post('http://url/to/api', files={'file_pro': my_file})

    # Check if the response is successful
    if response.status_code == 200:
        # Create a ContentFile from the response content
        zip_file = ContentFile(response.content)

        # Create a new instance of UploadedFile with the ContentFile
        uploaded_file = UploadedFile(file=zip_file)

        # Save the instance
        uploaded_file.save()
        print("File saved successfully.")
    else:
        print("Failed to retrieve the file:", response.status_code)

# Usage
my_file = open('path/to/local/file', 'rb')  # Replace with your local file path
save_zip_from_api()
