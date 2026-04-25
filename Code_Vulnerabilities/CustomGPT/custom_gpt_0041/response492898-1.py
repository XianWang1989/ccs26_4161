
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Update this with your actual app name

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Create a file-like object from the response content
zip_file_data = BytesIO(res.content)

# Optional: Check if the content type is indeed zip
if res.headers.get('Content-Type') == 'application/zip':
    # Step 3: Save the zip file to Django FileField
    zip_file_instance = UploadedFile()
    zip_file_instance.file.save('my_file.zip', ContentFile(zip_file_data.read()), save=True)

# Now, zip_file_instance will have the uploaded zip file.
