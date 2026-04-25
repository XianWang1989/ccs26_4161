
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check for a successful response
if res.status_code == 200:
    # Step 2: Use ContentFile to wrap the response content
    zip_content = ContentFile(res.content)

    # Step 3: Create the UploadedFile instance
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_zip_file.zip', zip_content, save=True)
else:
    print(f"Error: {res.status_code} - {res.text}")
