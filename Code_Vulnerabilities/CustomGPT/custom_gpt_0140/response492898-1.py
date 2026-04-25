
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from yourapp.models import UploadedFile  # Adjust the import to your app structure

# Make the POST request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is valid
if response.status_code == 200:
    # Assuming the response content is indeed a zip file
    zip_content = response.content

    # Create a Django file-like object
    zip_file = ContentFile(zip_content)

    # Create the UploadedFile instance
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded.zip', zip_file)  # Save it with a specific name
    uploaded_file.save()
else:
    print("Failed to retrieve the zip file:", response.status_code)
