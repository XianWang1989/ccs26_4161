
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from your_app.models import UploadedFile  # Update with your actual import

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Ensure the response is valid and get the content
if response.status_code == 200:
    # Creating a ContentFile from the response content
    zip_file_content = response.content
    content_file = ContentFile(zip_file_content, name='downloaded_file.zip')

    # Step 3: Save it to the UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', content_file, save=True)

    print("File saved successfully!")
else:
    print("Failed to retrieve the file:", response.status_code)
