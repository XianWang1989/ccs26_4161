
import requests
from io import BytesIO
from django.core.files import File
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Save the zip file to the model's file field
    uploaded_file.file.save('my_zip_file.zip', File(zip_file))

    # Optionally save the model instance if needed
    uploaded_file.save()
else:
    print(f"Error: {res.status_code}")
