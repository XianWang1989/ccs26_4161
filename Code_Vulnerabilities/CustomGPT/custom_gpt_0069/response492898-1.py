
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response is successful
if res.status_code == 200:
    # Create a file name for the uploaded file
    filename = 'my_uploaded_file.zip'

    # Use ContentFile to store the response content
    file_content = ContentFile(res.content)

    # Save the file to the default storage and create an UploadedFile instance
    uploaded_file = UploadedFile(file=default_storage.save(filename, file_content))
    uploaded_file.save()

    print("File saved successfully.")
else:
    print(f"Error: {res.status_code}")
