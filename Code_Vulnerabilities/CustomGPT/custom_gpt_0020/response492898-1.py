
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from .models import UploadedFile  # Adjust the import according to your project structure

def download_zip_and_save():
    # Make the request to the API to get the zip file
    res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

    if res.status_code == 200:
        # Get the content of the response
        zip_content = res.content  # This should be the binary data for the zip file

        # Create a ContentFile from the binary data
        zip_file = ContentFile(zip_content, name='downloaded.zip')

        # Now save this to your UploadedFile model
        uploaded_file_instance = UploadedFile(file=zip_file)
        uploaded_file_instance.save()
    else:
        print("Failed to download the file, status code:", res.status_code)

# Ensure this function is called in the appropriate context within your Django application
