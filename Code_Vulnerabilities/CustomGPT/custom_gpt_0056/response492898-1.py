
import requests
from django.core.files.base import ContentFile
from .models import UploadedFile

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if response.ok:
    # Step 2: Create a ContentFile from the response content
    zip_file_content = ContentFile(response.content)

    # Step 3: Create an UploadedFile instance and save it
    uploaded_file_instance = UploadedFile(file=zip_file_content)

    # Save the instance
    uploaded_file_instance.save()
else:
    # Handle error if needed
    print(f"Error occurred: {response.status_code}, {response.text}")
