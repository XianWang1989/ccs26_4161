
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Making the API request
url = 'http://url/to/api'
files = {'file_pro': open('path/to/your/input_file', 'rb')}  # Replace with your actual file path
res = requests.post(url, files=files)

if res.status_code == 200:
    # Define the name for the zip file to be saved
    zip_filename = 'response.zip'

    # Save the zip file in Django's storage
    # ContentFile wraps the response content, enabling it to be saved to Django's FileField
    zip_file_content = ContentFile(res.content)

    # Use default_storage to save the file
    file_path = default_storage.save(zip_filename, zip_file_content)

    # Create the UploadedFile instance
    uploaded_file = UploadedFile(file=file_path)
    uploaded_file.save()

    print(f'Successfully saved the zip file at {file_path}')
else:
    print(f'Failed to get the zip file. Status code: {res.status_code}')
