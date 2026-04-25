
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from myapp.models import UploadedFile  # Adjust the import as per your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_file_content = ContentFile(response.content)

    # Step 4: Save the file in your Django model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file_content)

    # Optionally: Save the instance if it’s new
    uploaded_file_instance.save()

    print("File saved successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)
