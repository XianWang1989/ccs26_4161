
import requests
from django.core.files.base import ContentFile
from io import BytesIO
import zipfile
from .models import UploadedFile  # Adjust the import based on your application structure

# Make the API request to get the zip file
url = 'http://url/to/api'
response = requests.post(url, files={'file_pro': *my_file*})

# Ensure the request was successful
if response.status_code == 200:
    # Use BytesIO for binary data
    zip_file = BytesIO(response.content)

    # Optionally, checking if it is indeed a zip file
    if zipfile.is_zipfile(zip_file):
        # Create an UploadedFile instance
        uploaded_file = UploadedFile()

        # Save the zip content into the model's FileField
        zip_file.seek(0)  # Reset the BytesIO object to the beginning
        uploaded_file.file.save('my_uploaded_file.zip', ContentFile(zip_file.read()), save=True)
    else:
        print("The response content is not a valid zip file.")
else:
    print(f"Failed to retrieve zip file: {response.status_code}")
