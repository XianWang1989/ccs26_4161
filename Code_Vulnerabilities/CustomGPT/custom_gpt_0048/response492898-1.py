
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from zipfile import ZipFile
from myapp.models import UploadedFile

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Handle the zip file (optional, if you need to check its contents)
    with ZipFile(zip_file) as z:
        # List files in the zip for debugging
        print(z.namelist())

    # Step 5: Save the zip file to the Django model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_zip_file.zip', ContentFile(response.content), save=True)
else:
    print(f"Error: {response.status_code}")
