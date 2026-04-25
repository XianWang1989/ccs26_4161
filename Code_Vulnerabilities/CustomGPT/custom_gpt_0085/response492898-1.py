
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from .models import UploadedFile

# Example API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Ensure the request was successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Create a ContentFile from the BytesIO object
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Save it to your UploadedFile model
    uploaded_file = UploadedFile(file=content_file)
    uploaded_file.save()
else:
    print("Failed to download file:", res.status_code)
