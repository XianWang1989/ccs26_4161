
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': open('path/to/local/file', 'rb')})

if res.status_code == 200:
    # Step 2: Create a file-like object from the response content
    zip_file = ContentFile(res.content, name='response.zip')

    # Step 3: Save to UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save(zip_file.name, zip_file)
    uploaded_file.save()

    print("Zip file saved successfully!")
else:
    print("Error:", res.status_code)
