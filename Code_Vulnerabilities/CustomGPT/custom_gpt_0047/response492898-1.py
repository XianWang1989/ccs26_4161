
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from yourapp.models import UploadedFile  # Adjust import as necessary

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a file-like object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Create a Django ContentFile from the BytesIO object
    content_file = ContentFile(zip_file.getvalue(), name='your_zip_file.zip')

    # Step 5: Create an instance of UploadedFile and save it
    uploaded_file_instance = UploadedFile(file=content_file)
    uploaded_file_instance.save()
else:
    print("Failed to retrieve the ZIP file.")
