
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Read the content of the response, which is the zip file
    zip_content = res.content

    # Create a file-like object from the bytes
    zip_file = BytesIO(zip_content)

    # Create a ContentFile to save to Django FileField
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Save the file to the UploadedFile model
    uploaded_file_instance = UploadedFile(file=content_file)
    uploaded_file_instance.save()
else:
    print("Error:", res.status_code)
