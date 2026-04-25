
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Adjust the import according to your project structure

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful
if res.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Step 4: Create a new UploadedFile instance
    uploaded_file = UploadedFile()

    # Save the zip file to the FileField
    uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_file.getvalue()), save=True)
else:
    print("Failed to get the zip file. Status code:", res.status_code)
