
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Replace with your actual app name

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.status_code == 200:
    # Use BytesIO to handle the binary data
    zip_file = BytesIO(res.content)

    # Create a ContentFile from the zip data
    content_file = ContentFile(zip_file.getvalue(), name='your_file.zip')

    # Save to your UploadedFile model
    my_file_instance = UploadedFile(file=content_file)
    my_file_instance.save()

else:
    print("Error: ", res.status_code)
