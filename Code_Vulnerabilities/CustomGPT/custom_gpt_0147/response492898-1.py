
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile
from your_app.models import UploadedFile

# Step 1: Make a request to the API
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful and the content is not empty
if response.status_code == 200 and response.content:
    # Convert response content to BytesIO
    zip_file = BytesIO(response.content)

    # Step 3: Save the zip file to Django's FileField
    # Create a content file from the BytesIO object
    content_file = ContentFile(zip_file.getvalue(), 'filename.zip')

    # Create an UploadedFile instance and save it
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('filename.zip', content_file)

    # Save the instance (if you need to persist it in the database)
    uploaded_file_instance.save()
else:
    print(f"Failed to retrieve zip file. Status code: {response.status_code}")
