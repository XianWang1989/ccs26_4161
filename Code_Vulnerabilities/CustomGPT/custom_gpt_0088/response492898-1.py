
import requests
from django.core.files import File
from django.core.files.base import ContentFile
from io import BytesIO
from .models import UploadedFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Create an UploadedFile instance
    uploaded_file = UploadedFile()

    # Use ContentFile to create a File object from BytesIO
    uploaded_file.file.save('my_file.zip', ContentFile(zip_file.getvalue()), save=True)

    print("File saved successfully.")
else:
    print("Failed to retrieve the zip file.")
