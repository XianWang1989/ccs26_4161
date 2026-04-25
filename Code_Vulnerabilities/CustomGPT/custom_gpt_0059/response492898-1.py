
import requests
import zipfile
import io
from django.core.files import File
from your_app.models import UploadedFile  # Adjust your import according to your app structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if res.status_code == 200:
    # Create a BytesIO stream from the response content
    zip_file_stream = io.BytesIO(res.content)

    # Optionally, verify this is a valid zip
    with zipfile.ZipFile(zip_file_stream) as zf:
        # If needed, list the contents or perform other checks
        print(zf.namelist())

    # Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Create a Django File object from the in-memory zip file
    uploaded_file.file.save('filename.zip', File(zip_file_stream), save=True)
else:
    print("Failed to retrieve the zip file:", res.status_code)
