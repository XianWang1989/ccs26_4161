
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from .models import UploadedFile  # Adjust the import according to your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful
if response.ok:
    # Step 3: Use BytesIO to create a file-like object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Create a ContentFile to hold the zip file
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Step 5: Now, create an instance of your UploadedFile model and save content
    uploaded_file = UploadedFile.objects.create(file=content_file)

    # Output to verify (optional)
    print("File uploaded successfully:", uploaded_file.file.url)
else:
    print("Failed to retrieve the zip file:", response.status_code)
