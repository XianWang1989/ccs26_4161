
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the request was successful
if response.status_code == 200:
    # Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Save the zip file to FileField
    zip_filename = 'my_uploaded_file.zip'  # Define the name for your zip file
    uploaded_file.file.save(zip_filename, ContentFile(response.content))

    # Optionally, save the model instance
    uploaded_file.save()

    print("File uploaded successfully!")
else:
    print("Failed to retrieve file:", response.status_code)
