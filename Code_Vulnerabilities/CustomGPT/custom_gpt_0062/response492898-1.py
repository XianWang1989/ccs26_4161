
import requests
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Import your model

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Create a file-like object from the response content
    zip_file = ContentFile(response.content, name='downloaded_file.zip')

    # Step 3: Save to your UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file)

    # Optionally, save the instance
    uploaded_file_instance.save()
else:
    print("Failed to fetch the zip file:", response.status_code)
