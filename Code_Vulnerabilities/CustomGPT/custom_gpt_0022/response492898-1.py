
import requests
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Ensure to import your UploadedFile model

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Step 2: Create a ContentFile from the response content
    zip_content = ContentFile(response.content, name='downloaded_file.zip')

    # Step 3: Save the file to the UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_content)
    uploaded_file_instance.save()
else:
    print("Failed to retrieve the zip file:", response.status_code)
