
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files import File
import io
from zipfile import ZipFile
from .models import UploadedFile  # Adjust the import based on your project structure

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the request was successful
if res.status_code == 200:
    # Step 3: Create an InMemoryUploadedFile from the response content
    zip_file_content = ContentFile(res.content)

    # Step 4: Create an UploadedFile instance
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_zip_file.zip', zip_file_content)

    # Step 5: Save the instance to the database
    uploaded_file.save()
else:
    print(f"Error: {res.status_code} - {res.text}")
