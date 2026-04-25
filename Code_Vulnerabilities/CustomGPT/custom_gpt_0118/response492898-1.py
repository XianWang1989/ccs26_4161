
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = BytesIO(response.content)

    # Save the ZIP file to the UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_file_content.getvalue()))
    uploaded_file.save()

    print("ZIP file successfully saved.")
else:
    print("Failed to retrieve ZIP file:", response.status_code)
