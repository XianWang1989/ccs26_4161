
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from myapp.models import UploadedFile

def save_zip_from_api():
    # Make the POST request to the API
    res = requests.post('http://url/to/api', files={'file_pro': ('filename.ext', open('path_to_your_file', 'rb'))})

    if res.status_code == 200:
        # Create a BytesIO stream from the response content
        zip_file = BytesIO(res.content)

        # Create a ContentFile to wrap the BytesIO stream
        content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

        # Create and save the UploadedFile instance
        uploaded_file = UploadedFile(file=content_file)
        uploaded_file.save()
        print(f"File saved: {uploaded_file.file.url}")
    else:
        print("Failed to download the zip file.")
