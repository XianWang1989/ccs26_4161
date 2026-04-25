
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

def save_zip_from_api(api_url):
    # Make the API call
    response = requests.post(api_url, files={'file_pro': 'my_file_content'})  # Add your actual file part here

    if response.status_code == 200:
        # Get the content of the zip file
        zip_content = response.content

        # Create a content file
        content_file = ContentFile(zip_content, name='downloaded_file.zip')

        # Save the UploadedFile instance
        uploaded_file_instance = UploadedFile()
        uploaded_file_instance.file.save('downloaded_file.zip', content_file)

        return uploaded_file_instance
    else:
        raise Exception(f"API call failed with status code: {response.status_code}")

# Example usage
uploaded_file = save_zip_from_api('http://url/to/api')
