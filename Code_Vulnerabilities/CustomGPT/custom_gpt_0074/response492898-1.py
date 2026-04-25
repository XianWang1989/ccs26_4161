
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from django.conf import settings
from .models import UploadedFile  # Assume your model is in models.py

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = ContentFile(res.content)

    # Create an instance of your UploadedFile model
    uploaded_file_instance = UploadedFile()

    # Save the file to the FileField
    uploaded_file_instance.file.save('filename.zip', zip_file)

    # Save the model instance to the database
    uploaded_file_instance.save()

    print("File saved successfully.")
else:
    print("Error while fetching the zip file.")
