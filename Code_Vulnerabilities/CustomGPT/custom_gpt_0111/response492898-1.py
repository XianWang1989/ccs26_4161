
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile
from your_app.models import UploadedFile  # adjust import based on your app structure

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response was successful
if response.status_code == 200:

    # Get the content of the zip file
    zip_content = response.content

    # Create an InMemoryUploadedFile
    zip_file = InMemoryUploadedFile(
        file=BytesIO(zip_content),
        field_name=None,
        name='downloaded_file.zip',
        content_type='application/zip',
        size=len(zip_content),
        charset=None
    )

    # Save the file to the UploadedFile model
    uploaded_file_instance = UploadedFile(file=zip_file)
    uploaded_file_instance.save()

else:
    print("Error fetching the file:", response.status_code)
