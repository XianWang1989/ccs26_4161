
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile

# Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Check if the response contains content
    zip_content = response.content

    # Create an InMemoryUploadedFile from the zip content
    zip_file = ContentFile(zip_content)
    my_uploaded_file = InMemoryUploadedFile(
        zip_file,
        None,
        'my_zipfile.zip',
        'application/zip',
        zip_file.size,
        None
    )

    # Save to Django model
    uploaded_file_instance = UploadedFile(file=my_uploaded_file)
    uploaded_file_instance.save()
else:
    print(f"Error: {response.status_code}")
