
import io
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Update with your actual app name

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if response.status_code == 200:
    # Create a file-like object from the response content
    zip_file = io.BytesIO(response.content)

    # You can create a ContentFile to attach to a FileField
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Save it to your model
    uploaded_file_instance = UploadedFile(file=content_file)
    uploaded_file_instance.save()
else:
    print(f"Error: {response.status_code} - {response.text}")
