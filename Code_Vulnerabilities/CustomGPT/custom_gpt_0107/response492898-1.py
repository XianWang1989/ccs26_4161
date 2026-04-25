
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import UploadedFile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Ensure the response is a zip file
if res.status_code == 200:
    # Step 3: Use ContentFile to wrap the binary content
    zip_content = ContentFile(res.content)

    # Step 4: Save the zip file to the model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('your_zip_file.zip', zip_content)

    # Optional: save the UploadedFile instance if not already done
    uploaded_file.save()
else:
    print(f"Failed to retrieve file: {res.status_code}")
