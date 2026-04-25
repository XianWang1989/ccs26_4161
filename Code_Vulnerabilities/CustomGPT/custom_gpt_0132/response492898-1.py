
import requests
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Create a ContentFile from response content
    zip_file_content = ContentFile(response.content)

    # Step 4: Create an instance of UploadedFile
    uploaded_file_instance = UploadedFile()

    # Step 5: Save the file with a name
    uploaded_file_instance.file.save('your_zip_file.zip', zip_file_content)

    # Step 6: Save the model instance
    uploaded_file_instance.save()

    print("Zip file uploaded successfully.")
else:
    print("Failed to fetch the zip file:", response.status_code)
