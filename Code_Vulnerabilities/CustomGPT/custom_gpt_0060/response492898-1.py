
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import UploadedFile  # Adjust the import statement according to your project structure

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Ensure we got a successful response
if response.status_code == 200:
    # Step 3: Create an in-memory binary stream from the response content
    zip_file = BytesIO(response.content)

    # Optionally, you may want to rename the file
    zip_file_name = 'downloaded_file.zip'

    # Step 4: Create an InMemoryUploadedFile instance
    uploaded_file = InMemoryUploadedFile(zip_file, 
                                         None,  # field name (not used)
                                         zip_file_name, 
                                         'application/zip', 
                                         zip_file.getbuffer().nbytes, 
                                         None)  # Content type (not used)

    # Step 5: Create and save the UploadedFile instance
    instance = UploadedFile()
    instance.file.save(zip_file_name, uploaded_file)

    # Optionally, you may want to save the instance itself if there's any other field
    instance.save()
else:
    print("Error in API request:", response.status_code, response.text)
