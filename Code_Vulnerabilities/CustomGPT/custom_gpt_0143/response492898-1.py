
import requests
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Replace with your actual app and model names

# Make the API call and get the response
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if res.status_code == 200:
    # Create a ContentFile from the response content
    zip_file_content = ContentFile(res.content, name='downloaded_file.zip')

    # Save to UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file_content)

    # Optionally, save the instance to the database
    uploaded_file_instance.save()
else:
    print("Error:", res.status_code)
