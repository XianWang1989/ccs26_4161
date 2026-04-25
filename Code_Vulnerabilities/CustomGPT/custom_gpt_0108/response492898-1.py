
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from yourapp.models import UploadedFile

# Make the API call to get the zip file
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response was successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Create ContentFile to save the zip file
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Assign the ContentFile to the FileField and save
    uploaded_file.file.save('downloaded_file.zip', content_file)
    uploaded_file.save()
else:
    print(f"Error: {response.status_code}")
