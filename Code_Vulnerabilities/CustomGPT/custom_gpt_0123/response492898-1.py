
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from myapp.models import UploadedFile  # Import your model

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': 'your_file_here'})

if res.ok:
    # Step 2: Wrap the response content in a BytesIO object
    zip_file = BytesIO(res.content)

    # Step 3: Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Step 4: Save the BytesIO content to the FileField
    uploaded_file.file.save('filename.zip', ContentFile(zip_file.getvalue()), save=True)

    print("File saved successfully!")
else:
    print("Failed to retrieve the file.")
