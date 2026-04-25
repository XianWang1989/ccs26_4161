
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if res.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_content = ContentFile(res.content, name='my_zip_file.zip')

    # Step 4: Create an instance of UploadedFile
    uploaded_file = UploadedFile(file=zip_content)

    # Step 5: Save the instance to the database
    uploaded_file.save()
else:
    print(f"Error: {res.status_code} - {res.text}")
