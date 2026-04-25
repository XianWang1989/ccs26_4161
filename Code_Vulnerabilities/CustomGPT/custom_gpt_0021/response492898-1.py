
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from yourapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if response.status_code == 200:
    # Step 3: Create a Django ContentFile from the response content
    zip_file = ContentFile(response.content)

    # Step 4: Save it to the UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file)

    # Step 5: (Optional) To save the instance, if needed
    uploaded_file_instance.save()

    print("Zip file saved successfully.")
else:
    print("Failed to retrieve the zip file. Status code:", response.status_code)
