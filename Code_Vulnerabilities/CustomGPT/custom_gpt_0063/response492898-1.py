
import requests
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

def save_zip_file_to_model():
    # Step 1: Send the request to the API
    res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

    # Step 2: Create an InMemoryUploadedFile
    zip_content = res.content  # This should contain the binary content of the zip
    zip_file = io.BytesIO(zip_content)
    zip_file.name = 'downloaded.zip'  # Set a name for the file

    # Create InMemoryUploadedFile
    uploaded_file = InMemoryUploadedFile(
        file=zip_file,
        field_name=None,
        name=zip_file.name,
        content_type='application/zip',
        size=len(zip_content),
        charset=None
    )

    # Step 3: Save to the model
    uploaded_instance = UploadedFile(file=uploaded_file)
    uploaded_instance.save()

# Call the function
save_zip_file_to_model()
