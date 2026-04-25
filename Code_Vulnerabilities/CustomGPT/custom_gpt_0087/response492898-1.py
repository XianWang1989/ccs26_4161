
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Replace with your actual app and model name

# Step 1: Call the API
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a BytesIO instance from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Create a ContentFile to save it to the UploadedFile model
    content_file = ContentFile(zip_file.getvalue(), name='my_file.zip')

    # Step 5: Save the UploadedFile instance
    uploaded_file_instance = UploadedFile(file=content_file)
    uploaded_file_instance.save()
else:
    print(f"Failed to retrieve the file: {response.status_code}")
