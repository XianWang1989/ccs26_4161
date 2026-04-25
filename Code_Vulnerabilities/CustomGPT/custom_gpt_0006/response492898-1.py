
import requests
import tempfile
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

def fetch_and_save_zip():
    # Step 1: Make the API call
    res = requests.post('http://url/to/api', files={'file_pro': 'your_file_here'})

    if res.status_code == 200:
        # Step 2: Create a temporary file to hold the zip content
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
            temp_zip.write(res.content)  # Write the content of the response to the temp file
            temp_zip.seek(0)  # Move to the start of the file

            # Step 3: Create a Django UploadedFile instance
            uploaded_file = InMemoryUploadedFile(
                temp_zip,
                None,
                'your_zip_file.zip',
                'application/zip',
                temp_zip.tell(),  # Size of the file
                None
            )

            # Step 4: Save the UploadedFile instance
            instance = UploadedFile(file=uploaded_file)
            instance.save()

    else:
        print("Failed to retrieve the zip file:", res.status_code)

# Call the function to perform the operation
fetch_and_save_zip()
