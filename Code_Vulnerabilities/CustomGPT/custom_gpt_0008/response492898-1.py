
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from .models import UploadedFile  # Adjust the import based on your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Step 2: Create a ContentFile from the response content
    zip_file_content = ContentFile(response.content)

    # Step 3: Save the file into the UploadedFile model
    uploaded_file = UploadedFile()

    # Step 4: Save the file to the FileField
    uploaded_file.file.save('downloaded_file.zip', zip_file_content, save=True)  # Use appropriate filename

    # Now you can access uploaded_file instance if needed
    print("File saved successfully:", uploaded_file.file.url)
else:
    print("Failed to retrieve the file:", response.status_code)
