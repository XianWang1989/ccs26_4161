
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from io import BytesIO

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

# Call the API and get the response
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Assuming the content type returned is that of a zip file
    zip_content = response.content

    # Create a BytesIO object from the zip content
    zip_file = BytesIO(zip_content)

    # Save the uploaded zip file using Django's file handling
    uploaded_file = UploadedFile()
    # Generate a filename (you can customize this based on your needs)
    filename = 'my_uploaded_file.zip'

    # Create a ContentFile instance and save it to the model
    uploaded_file.file.save(filename, ContentFile(zip_file.getvalue()))
    uploaded_file.save()
    print("Zip file uploaded successfully!")
else:
    print("Error fetching the zip file:", response.status_code)
