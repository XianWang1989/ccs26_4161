
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile
from .models import UploadedFile  # Adjust this import based on your project structure

# Make the API call to get the zip file
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_content = BytesIO(res.content)

    # Save the zip file to Django's UploadedFile model
    uploaded_file = UploadedFile()

    # Create an InMemoryUploadedFile from the zip content
    uploaded_file.file.save('uploaded.zip', ContentFile(zip_content.getvalue()), save=True)

    # Now, uploaded_file has the zip saved in the FileField
else:
    print("Error fetching the zip file: ", res.status_code)
