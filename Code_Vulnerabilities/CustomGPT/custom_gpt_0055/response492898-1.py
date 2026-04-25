
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile
from myapp.models import UploadedFile  # Adjust the import according to your app structure

# Make the API call and get the zip file data
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response is successful
if response.status_code == 200:
    # Create a BytesIO stream from the response content
    zip_file_data = BytesIO(response.content)

    # Optionally: Test if it's a zip file (not necessary for saving, but good practice)
    try:
        with ZipFile(zip_file_data) as zip_file:
            zip_file.extractall('/path/to/extract')  # specify the path if needed
    except Exception as e:
        print(f"Error extracting zip file: {e}")

    # Create an InMemoryUploadedFile instance
    uploaded_file = InMemoryUploadedFile(
        file=zip_file_data,
        field_name=None,
        name='my_file.zip',
        content_type='application/zip',
        size=len(response.content),
        charset=None
    )

    # Save the uploaded file to the model
    my_uploaded_file = UploadedFile(file=uploaded_file)
    my_uploaded_file.save()
else:
    print("Failed to retrieve file, status code:", response.status_code)
