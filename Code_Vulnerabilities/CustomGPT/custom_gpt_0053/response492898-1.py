
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call and receive the zip file
url = 'http://url/to/api'
res = requests.post(url, files={'file_pro': my_file})

# Step 2: Ensure to check if the request was successful
if res.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_content = ContentFile(res.content)

    # Step 4: Create the UploadedFile instance
    uploaded_file = UploadedFile()

    # Step 5: Save the ContentFile to the FileField
    uploaded_file.file.save('my_zip_file.zip', zip_content)

    # Step 6: Save the UploadedFile instance to the database
    uploaded_file.save()
else:
    print("Failed to retrieve the file, status code:", res.status_code)
