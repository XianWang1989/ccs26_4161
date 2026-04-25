
import requests
import tempfile
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models

# Your Django model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

def save_zip_from_api(url):
    # Make the API request
    res = requests.post(url, files={'file_pro': my_file})

    if res.status_code == 200:
        # Create a temporary file
        temp_file = NamedTemporaryFile(delete=False)
        temp_file.write(res.content)
        temp_file.close()

        # Create an UploadedFile instance
        with open(temp_file.name, 'rb') as f:
            uploaded_file = UploadedFile()
            uploaded_file.file.save('my_zip_file.zip', File(f))
            uploaded_file.save()

        # Clean up the temporary file if needed
        # os.remove(temp_file.name)
        return uploaded_file
    else:
        raise Exception("Failed to download zip file")

# Example usage:
# uploaded_file_instance = save_zip_from_api('http://url/to/api')
