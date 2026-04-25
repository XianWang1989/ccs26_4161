
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from .models import UploadedFile  # Adjust the import based on your project structure

# API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Ensure the response is successful and is of a zip file type
if res.status_code == 200 and res.headers['Content-Type'] == 'application/zip':
    # Create BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Save to Django model
    uploaded_file = UploadedFile()  # Create a new instance of your model
    uploaded_file.file.save('my_uploaded_file.zip', ContentFile(zip_file.getvalue()))
    uploaded_file.save()  # Save the model instance
else:
    print("Failed to retrieve the zip file")
