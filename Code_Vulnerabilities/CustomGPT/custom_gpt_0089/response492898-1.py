
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from .models import UploadedFile  # Import your model

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check for successful response
if response.status_code == 200:
    # Step 2: Create a ContentFile from the response content
    zip_content = ContentFile(response.content, name='downloaded_file.zip')

    # Step 3: Save to your Django model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_content)

    # Optional: Save the instance if needed
    uploaded_file_instance.save()
else:
    print("Error:", response.status_code)
