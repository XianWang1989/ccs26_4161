
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Step 1: Make the request to the API
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the request was successful
if response.status_code == 200:
    # Step 2: Create an in-memory file object
    zip_file = BytesIO(response.content)

    # Step 3: Save the file to your model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded_file.zip', ContentFile(zip_file.getvalue()))

    # Optionally save the model instance
    uploaded_file.save()
else:
    print(f"Failed to retrieve the file: {response.status_code}")
