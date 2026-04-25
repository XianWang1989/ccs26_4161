
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from your_app.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Create an in-memory file from the zip content
    zip_file = ContentFile(res.content, name='downloaded_file.zip')

    # Save the file to your UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded_file.zip', zip_file)
    uploaded_file.save()
else:
    print("Failed to retrieve zip file")
