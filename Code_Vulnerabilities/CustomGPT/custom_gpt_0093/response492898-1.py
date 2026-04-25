
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from myapp.models import UploadedFile  # Adjust according to your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': your_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Save the zip file to the UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded_file.zip', ContentFile(zip_file.getvalue()), save=True)
else:
    print(f"Error: {response.status_code}")
