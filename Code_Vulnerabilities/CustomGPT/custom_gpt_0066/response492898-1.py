
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from your_app.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': your_file})

# Step 2: Ensure request was successful
if res.status_code == 200:
    # Step 3: Create an InMemoryUploadedFile from the response content
    content = BytesIO(res.content)
    uploaded_file = InMemoryUploadedFile(
        content=content,
        field_name=None,
        name='your_file_name.zip',  # Provide a suitable name
        content_type='application/zip',  # Specify content type
        size=len(res.content),
        charset=None
    )

    # Step 4: Save to your Django model
    file_instance = UploadedFile()
    file_instance.file.save(uploaded_file.name, uploaded_file, save=True)
else:
    print("Error: Unable to fetch the file from the API.")
