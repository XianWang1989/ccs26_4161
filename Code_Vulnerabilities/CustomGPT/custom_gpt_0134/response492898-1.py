
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    content_file = ContentFile(response.content)

    # Optional: Set a filename (with .zip extension)
    filename = 'downloaded_file.zip'

    # Step 4: Save the file to the UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save(filename, content_file)

    uploaded_file_instance.save()  # Don't forget to save the instance
else:
    print("Error:", response.status_code, response.text)
