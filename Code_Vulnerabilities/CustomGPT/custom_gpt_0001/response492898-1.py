
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from .models import UploadedFile  # Adjust the import based on your project structure

# Make the API call to receive the zip file
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response was successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_data = BytesIO(response.content)

    # Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Use ContentFile to create a file-like object that Django can save
    uploaded_file.file.save('my_uploaded_file.zip', ContentFile(zip_file_data.getvalue()))

    # Optionally save the instance if you have other fields to save
    uploaded_file.save()
else:
    print(f"Error: Received status code {response.status_code}")
