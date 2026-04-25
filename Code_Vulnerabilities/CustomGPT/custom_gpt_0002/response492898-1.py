
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust based on your app name

# Make the request to the API
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure response is successful
if res.status_code == 200:
    # Create a new UploadedFile instance
    my_file = UploadedFile()

    # Save the zip file content as a ContentFile
    my_file.file.save('downloaded_file.zip', ContentFile(res.content))
    my_file.save()
else:
    # Handle any errors if needed
    print(f"Error: {res.status_code}")
