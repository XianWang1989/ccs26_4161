
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from your_app.models import UploadedFile

# Step 1: Make the API call to get the zip file
response = requests.post('http://url/to/api', files={'file_pro': ('my_file', open('path/to/local/file', 'rb'))})

if response.status_code == 200:
    # Step 2: Convert response content to a BytesIO object
    zip_file = BytesIO(response.content)

    # Step 3: Create the UploadedFile instance and save it
    uploaded_file = UploadedFile()
    uploaded_file.file.save('your_zip_file.zip', ContentFile(zip_file.getvalue()), save=True)

    print("File saved successfully.")
else:
    print("Failed to retrieve the zip file.")
