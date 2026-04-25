
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from myapp.models import UploadedFile  # Adjust the import according to your app structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.status_code == 200:
    # Create a ContentFile from the response content
    zip_content = ContentFile(res.content)

    # Create the UploadedFile instance
    my_file = UploadedFile()
    my_file.file.save('my_zip_file.zip', zip_content)  # Use the desired filename
    my_file.save()
else:
    print("Failed to retrieve the zip file:", res.status_code)
