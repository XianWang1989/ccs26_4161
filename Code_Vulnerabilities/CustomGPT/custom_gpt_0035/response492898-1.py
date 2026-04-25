
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from your_app.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = BytesIO(res.content)

    # Create a new UploadedFile instance and save the file
    uploaded_file = UploadedFile()
    # Use ContentFile to convert the BytesIO content to a FileField-compatible format
    uploaded_file.file.save('downloaded_file.zip', ContentFile(zip_file_content.getvalue()))
    uploaded_file.save()
else:
    print(f"Error: {res.status_code}")
