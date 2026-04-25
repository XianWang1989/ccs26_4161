
import requests
from django.core.files.base import ContentFile
from django.core.files.base import File
from your_app.models import UploadedFile  # Adjust the import according to your project structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the API call was successful (status code 200)
if res.status_code == 200:
    # Create a ContentFile from the binary response content
    zip_file_content = ContentFile(res.content)

    # Create your UploadedFile instance and save it
    my_uploaded_file = UploadedFile()
    my_uploaded_file.file.save('filename.zip', zip_file_content)  # Adjust filename as needed
    my_uploaded_file.save()
else:
    print("Failed to download ZIP file:", res.status_code)
