
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile  # Adjust the import to match your app structure

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Ensure the response is successful and contain content
if res.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_content = ContentFile(res.content, name='downloaded.zip')

    # Step 4: Save the ContentFile to your UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded.zip', zip_content)

    # Optional: Save the instance to the database
    uploaded_file_instance.save()
else:
    print(f"Error: {res.status_code} - {res.text}")
