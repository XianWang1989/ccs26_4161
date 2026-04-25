
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Adjust this import according to your app structure

# Make the request to the API
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create an InMemoryUploadedFile from the response content
    file_name = 'response.zip'  # or any name you prefer
    file_content = ContentFile(res.content)
    uploaded_file = InMemoryUploadedFile(file_content, None, file_name, 'application/zip', res.content.__sizeof__(), None)

    # Create an instance of the UploadedFile model and save it
    uploaded_instance = UploadedFile(file=uploaded_file)
    uploaded_instance.save()
else:
    print(f"Failed to retrieve zip file: {res.status_code}")
