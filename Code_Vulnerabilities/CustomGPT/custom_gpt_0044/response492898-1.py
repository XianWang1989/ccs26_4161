
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from io import BytesIO
from zipfile import ZipFile
from .models import UploadedFile  # Adjust the import according to your project structure

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the request was successful
if res.status_code == 200:
    # Step 3: Create a ZipFile object
    zip_file_content = BytesIO(res.content)

    # Optional: Validate the ZIP file contents (if needed)
    try:
        with ZipFile(zip_file_content) as zip_ref:
            zip_ref.testzip()  # This checks if the zip is valid
    except Exception as e:
        print(f"Invalid ZIP file: {e}")

    # Step 4: Save the ZIP file to UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_file.zip', ContentFile(res.content), save=True) # Saving the content directly

    print("File saved successfully.")
else:
    print(f"Failed to download file: {res.status_code}")
