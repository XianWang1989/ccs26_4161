
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Update with your actual app name

# Step 1: Make the API request
url = 'http://url/to/api'
res = requests.post(url, files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Step 2: Create a ContentFile from the response content
    zip_content = ContentFile(res.content, name='response.zip')

    # Step 3: Save the file to the model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('response.zip', zip_content)

    # Save the instance to the database
    uploaded_file_instance.save()
else:
    print("Failed to fetch the zip file. Status code:", res.status_code)
