
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import UploadedFile  # Adjust the import based on your app structure

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response is successful
response.raise_for_status()

# Create a file object from the response content
zip_file_content = response.content
zip_file_name = 'your_zip_file.zip'  # Adjust the file name as needed

# Create a ContentFile
content_file = ContentFile(zip_file_content)

# Save the file using Django's storage system
uploaded_file = UploadedFile()
uploaded_file.file.save(zip_file_name, content_file)

# Now you can save your model instance
uploaded_file.save()
