
import requests
from django.core.files.base import ContentFile
from django.core.files.base import File
from yourapp.models import UploadedFile

# Step 1: Make the API call to retrieve the zip file
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the request was successful
if res.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_file_content = ContentFile(res.content, name='downloaded_file.zip')

    # Step 4: Save the zip file to the UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('downloaded_file.zip', zip_file_content)

    # Step 5: Optionally save the model instance to the database
    uploaded_file.save()
else:
    print("Failed to retrieve zip file:", res.status_code)
