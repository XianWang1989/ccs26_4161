
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from zipfile import ZipFile
from yourapp.models import UploadedFile  # Adjust the import according to your app structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': your_file})

# Check if the request was successful
if res.status_code == 200:
    # Create a BytesIO stream from the response content
    zip_stream = BytesIO(res.content)

    # Optional: Verify if it's a valid zip file
    try:
        with ZipFile(zip_stream, 'r') as zip_file:
            # If needed, you can list contents here
            print(zip_file.namelist())  # Lists files in the zip
    except Exception as e:
        print(f"Invalid zip file: {e}")
        # Handle the error accordingly

    # Save the zip file content to a Django FileField
    uploaded_file = UploadedFile()
    uploaded_file.file.save('filename.zip', ContentFile(res.content))
    uploaded_file.save()

    print("File saved successfully.")
else:
    print(f"Failed to retrieve the file: {res.status_code}")
