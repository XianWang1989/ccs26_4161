
import requests
from io import BytesIO
from zipfile import ZipFile
from django.core.files.base import ContentFile
from .models import UploadedFile

# Make the request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Create a BytesIO stream from the response content
    zip_file_stream = BytesIO(res.content)

    # Optionally, you can verify the file is a valid zip file
    try:
        with ZipFile(zip_file_stream) as zip_file:
            # Process the zip if needed (e.g., extracting specific files)
            # For now, we will just read it as is to save it to UploadedFile
            uploaded_file_instance = UploadedFile(
                file=ContentFile(res.content, name='downloaded_file.zip')
            )
            uploaded_file_instance.save()
            print("File saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Failed to download file, status code: {res.status_code}")
