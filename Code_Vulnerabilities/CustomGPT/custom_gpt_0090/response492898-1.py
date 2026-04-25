
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if request was successful
if res.status_code == 200:
    # Create a ContentFile from the response content
    zip_content = ContentFile(res.content)

    # Create an instance of UploadedFile
    uploaded_file_instance = UploadedFile()

    # Save the ContentFile to the FileField
    uploaded_file_instance.file.save('my_zip_file.zip', zip_content)

    # Save the instance to the database
    uploaded_file_instance.save()
else:
    print(f"Error: {res.status_code}")
