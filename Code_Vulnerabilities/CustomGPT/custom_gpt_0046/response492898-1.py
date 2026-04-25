
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from myapp.models import UploadedFile  # Adjust import according to your app structure

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': open('your_file_path', 'rb')})

# Check if the response is successful
if response.status_code == 200:
    # Create an instance of UploadedFile
    uploaded_file = UploadedFile()

    # Use ContentFile to handle the bytes content received in the response
    uploaded_file.file.save('my_zip_file.zip', ContentFile(response.content))

    # Save the model instance
    uploaded_file.save()
else:
    print('Error:', response.status_code, response.text)
