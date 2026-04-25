
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from django.db import models

# Define your UploadedFile model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

# Function to save the zip file
def save_zip_file():
    response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

    if response.status_code == 200:
        # Create a BytesIO object from the response content
        zip_file = BytesIO(response.content)

        # Create an instance of UploadedFile and save the zip data
        uploaded_file_instance = UploadedFile()
        uploaded_file_instance.file.save('my_file.zip', ContentFile(zip_file.getvalue()))
        uploaded_file_instance.save()

        return uploaded_file_instance
    else:
        raise Exception("Failed to retrieve the zip file from the API.")

# Example usage
# my_uploaded_file = save_zip_file()
