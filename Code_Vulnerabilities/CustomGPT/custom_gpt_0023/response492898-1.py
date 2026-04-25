
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from yourapp.models import UploadedFile  # Adjust import based on your app structure
import zipfile

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if response.status_code == 200:
    # Create a BytesIO stream from the response content
    zip_file = BytesIO(response.content)

    # Validate if it's a zip file
    with zipfile.ZipFile(zip_file) as z:
        # If needed, list the zip contents
        print(z.namelist())  # List files in the zip

    # Reset the pointer of the BytesIO object
    zip_file.seek(0)

    # Create an InMemoryUploadedFile object
    uploaded_file = InMemoryUploadedFile(zip_file, None, 'downloaded.zip', 'application/zip', zip_file.getbuffer().nbytes, None)

    # Save to your UploadedFile model
    my_uploaded_file_instance = UploadedFile(file=uploaded_file)
    my_uploaded_file_instance.save()
else:
    print(f'Error: {response.status_code}')
