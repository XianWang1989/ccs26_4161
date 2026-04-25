
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call and get the zip file contents
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Create an UploadedFile instance and save the zip file
    zip_file_content = response.content  # Get the raw bytes of the zip file

    # Create a ContentFile from the zip file content
    content_file = ContentFile(zip_file_content)

    # Step 4: Use the UploadedFile model to save the file
    my_uploaded_file = UploadedFile()
    my_uploaded_file.file.save('downloaded_file.zip', content_file)  # Use an appropriate file name
    my_uploaded_file.save()

    print("File saved successfully.")
else:
    print(f"Error: {response.status_code}")
