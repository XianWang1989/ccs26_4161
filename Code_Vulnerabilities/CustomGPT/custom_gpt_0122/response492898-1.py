
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if response is successful
if res.status_code == 200:
    # Step 3: Create a zip file from the response content
    zip_content = BytesIO(res.content)

    # Step 4: Use InMemoryUploadedFile to handle the zip file
    uploaded_file = InMemoryUploadedFile(
        file=zip_content,
        field_name=None,
        name='downloaded.zip',
        content_type='application/zip',
        size=res.content.__len__(),
        charset=None
    )

    # Step 5: Save the UploadedFile instance
    my_uploaded_file = UploadedFile(file=uploaded_file)
    my_uploaded_file.save()

    print("File saved successfully!")
else:
    print(f"Failed to download file: {res.status_code}")
