
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful and contains a zip file
if response.status_code == 200:
    # Get the content as bytes
    zip_content = response.content

    # Step 3: Create a temporary InMemoryUploadedFile
    zip_file = InMemoryUploadedFile(
        file=BytesIO(zip_content),
        field_name=None,
        name='response.zip',
        content_type='application/zip',
        size=len(zip_content),
        charset=None
    )

    # Step 4: Save it to your UploadedFile model
    uploaded_file_instance = UploadedFile(file=zip_file)
    uploaded_file_instance.save()

    print("Zip file saved successfully!")
else:
    print("Failed to retrieve the zip file:", response.status_code)
