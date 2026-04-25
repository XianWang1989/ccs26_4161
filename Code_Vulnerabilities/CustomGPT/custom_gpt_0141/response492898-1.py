
import requests
import zipfile
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.db import models

# Assuming you have this model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='path/to/upload', max_length=255)

def save_zip_file_to_model(api_url, my_file):
    # Step 1: Make the API call
    res = requests.post(api_url, files={'file_pro': my_file})

    # Ensure the request was successful
    if res.status_code == 200:
        # Step 2: Create a binary stream from the response content
        zip_content = res.content

        # Optionally: Verify the content type (optional step)
        if 'application/zip' not in res.headers.get('Content-Type', ''):
            raise ValueError("Received content is not a zip file.")

        # Step 3: Create a new InMemoryUploadedFile
        zip_file_name = 'downloaded_file.zip'  # Replace with desired name
        zip_file = InMemoryUploadedFile(
            file=ContentFile(zip_content),
            field_name=None,
            name=zip_file_name,
            content_type='application/zip',
            size=len(zip_content),
            charset=None
        )

        # Step 4: Save the InMemoryUploadedFile to the model
        uploaded_file_instance = UploadedFile(file=zip_file)
        uploaded_file_instance.save()
    else:
        raise Exception("Failed to retrieve the zip file from the API.")

# Example usage
# my_file should be an actual file-like object you want to send to the API
# save_zip_file_to_model('http://url/to/api', my_file)
