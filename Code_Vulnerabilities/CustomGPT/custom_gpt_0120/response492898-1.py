
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Adjust the import according to your project structure

# Step 1: Call the API and get the zip file
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.status_code == 200:
    # Step 2: Create a ContentFile from the response content
    zip_file_content = ContentFile(res.content)

    # Step 3: Create an instance of UploadedFile
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded_file.zip', zip_file_content)  # Specify a file name

    # Step 4: Save the model instance
    uploaded_file.save()

    print("File saved successfully.")
else:
    print("Failed to download file:", res.status_code)
