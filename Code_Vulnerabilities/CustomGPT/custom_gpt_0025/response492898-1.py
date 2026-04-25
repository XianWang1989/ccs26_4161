
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile
from .models import UploadedFile  # Adjust the import based on your project structure

def save_zip_from_api():
    # Step 1: Call the API and receive the zip file
    res = requests.post('http://url/to/api', files={'file_pro': 'my_file'})

    if res.status_code == 200:
        # Step 2: Create a BytesIO object from the response content
        zip_file = BytesIO(res.content)

        try:
            # Step 3: Check if the content is a valid zip file
            with zipfile.ZipFile(zip_file, 'r') as zf:
                # Optionally: List the files in the zip
                print(zf.namelist())  # This will show you the contents of the zip

            # Step 4: Save to Django's FileField
            zip_file.seek(0)  # Reset buffer position to the beginning
            uploaded_file = InMemoryUploadedFile(
                zip_file,            # File object
                None,                # Field name (usually None unless specified)
                'my_file.zip',      # File name
                'application/zip',  # Content type
                zip_file.getbuffer().nbytes,  # Size of the zip file
                None                 # Charset (usually None for binary files)
            )

            # Step 5: Create and save your model instance
            file_instance = UploadedFile(file=uploaded_file)
            file_instance.save()
            print("File saved successfully.")

        except zipfile.BadZipFile:
            print("The response content is not a valid zip file.")
    else:
        print(f"Failed to retrieve file. Status code: {res.status_code}")
