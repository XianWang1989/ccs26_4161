
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
import zipfile
import io

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': <your_file_here>})

if res.status_code == 200:
    # Create an in-memory file storage object
    zip_file = InMemoryUploadedFile(
        io.BytesIO(res.content),  # Use BytesIO to wrap the response content
        None,
        'my_zip_file.zip',  # Name of the zip file
        'application/zip',
        res.headers.get('Content-Length', len(res.content)),
        None
    )

    # Save the file to your UploadedFile model
    uploaded_file = UploadedFile(file=zip_file)  # Assuming UploadedFile is your model
    uploaded_file.save()
else:
    print("Failed to retrieve the zip file:", res.status_code)
