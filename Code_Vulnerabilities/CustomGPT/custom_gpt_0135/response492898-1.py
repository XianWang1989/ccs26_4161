
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from django.db import models

# Your UploadedFile model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

# Function to call the API and save the zip file
def save_zip_from_api():
    # Make the API call
    res = requests.post('http://url/to/api', files={'file_pro': my_file})

    # Check for a successful response
    if res.status_code == 200:
        # Create a ContentFile from the response content
        content_file = ContentFile(res.content)
        # Instantiate your model and save the file
        uploaded_file = UploadedFile()
        uploaded_file.file.save('my_file.zip', content_file)
        uploaded_file.save()
        return uploaded_file
    else:
        raise Exception("API call failed with status: {}".format(res.status_code))
