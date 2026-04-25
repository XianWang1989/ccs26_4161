
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from yourapp.models import UploadedFile

# Step 1: Make the API call
url = 'http://url/to/api'
files = {'file_pro': open('path/to/local/file', 'rb')}
res = requests.post(url, files=files)

# Step 2: Check if the response is okay and get the content
if res.status_code == 200:
    file_content = res.content  # This is the zip file content
    file_name = 'response.zip'   # Name for your zip file

    # Step 3: Create an InMemoryUploadedFile
    uploaded_file = InMemoryUploadedFile(
        file=BytesIO(file_content),
        field_name=None,
        name=file_name,
        content_type='application/zip',
        size=len(file_content),
        charset=None
    )

    # Step 4: Save it to your UploadedFile model
    my_uploaded_file_instance = UploadedFile()
    my_uploaded_file_instance.file.save(file_name, uploaded_file, save=True)

    print("File saved successfully!")
else:
    print("Error fetching the zip file:", res.status_code)
