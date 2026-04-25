
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import UploadedFile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful
if res.status_code == 200:
    # Store the ZIP file content
    zip_content = res.content

    # Step 3: Create a ContentFile and save it
    zip_file_name = 'file.zip'  # You can customize the filename
    zip_file = ContentFile(zip_content, name=zip_file_name)

    # Step 4: Save the file to the model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save(zip_file.name, zip_file)

    # Optional: Save the instance to persist data
    uploaded_file_instance.save()

    print(f"File {zip_file_name} saved successfully.")
else:
    print("Failed to download the zip file.")
