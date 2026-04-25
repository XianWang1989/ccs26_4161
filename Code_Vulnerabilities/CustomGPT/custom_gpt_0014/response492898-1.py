
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models

# Your Django model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

# Function to download the zip file and save it
def download_and_save_zip():
    response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

    if response.status_code == 200:
        # Create a ContentFile from the response content
        zip_content = ContentFile(response.content)

        # Create the UploadedFile instance and save it
        uploaded_file = UploadedFile()
        uploaded_file.file.save('your_zip_file_name.zip', zip_content)
        uploaded_file.save()

        print("Zip file saved successfully.")
    else:
        print("Error downloading file:", response.status_code)

# Call the function
download_and_save_zip()
