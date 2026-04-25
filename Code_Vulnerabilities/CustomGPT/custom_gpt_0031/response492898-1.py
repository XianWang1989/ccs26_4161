
import requests
from django.core.files.base import ContentFile
from .models import UploadedFile

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Create a ContentFile from the response content
    zip_file = ContentFile(response.content, name='downloaded_file.zip')

    # Save the file to the UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file)
    uploaded_file_instance.save()
else:
    print("Failed to retrieve the file")
