
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from .models import UploadedFile

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Ensure the response is a zip file
if response.ok and response.headers['Content-Type'] == 'application/zip':
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Create a ContentFile from the BytesIO object
    content_file = ContentFile(zip_file.read(), name='downloaded_file.zip')

    # Step 5: Save the file to the UploadedFile model
    uploaded_file = UploadedFile(file=content_file)
    uploaded_file.save()

    print("File saved successfully.")
else:
    print("Failed to retrieve the zip file.")
