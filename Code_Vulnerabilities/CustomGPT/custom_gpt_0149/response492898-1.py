
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from your_app.models import UploadedFile  # Adjust the import according to your app structure

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check for successful response
if response.status_code == 200:
    # Step 3: Create a BytesIO stream from the response content
    zip_file_stream = BytesIO(response.content)

    # Step 4: Create a ContentFile from the BytesIO stream
    content_file = ContentFile(zip_file_stream.getvalue(), name='downloaded_file.zip')

    # Step 5: Save to UploadedFile model
    uploaded_file = UploadedFile(file=content_file)
    uploaded_file.save()
else:
    print(f"Error: {response.status_code}")
