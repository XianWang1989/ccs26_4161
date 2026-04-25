
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile
from yourapp.models import UploadedFile  # Adjust the import based on your project structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = BytesIO(res.content)

    # Optionally, check if content is indeed a zip file
    if zipfile.is_zipfile(zip_file_content):
        # Reset the pointer in case it was read
        zip_file_content.seek(0)

        # Create an InMemoryUploadedFile
        uploaded_file = InMemoryUploadedFile(zip_file_content, None, 'downloaded_file.zip', 'application/zip', zip_file_content.getbuffer().nbytes, None)

        # Save the file to your model
        my_uploaded_file_instance = UploadedFile()
        my_uploaded_file_instance.file.save('downloaded_file.zip', uploaded_file)
        my_uploaded_file_instance.save()
        print("File saved successfully.")
    else:
        print("Response is not a valid zip file.")
else:
    print(f"Failed to retrieve file: {res.status_code}")
