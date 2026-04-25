
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import UploadedFile  # Adjust the import according to your project structure

def fetch_and_save_zip():
    # Step 1: Make the API call
    res = requests.post('http://url/to/api', files={'file_pro': my_file})

    # Step 2: Check if the response is successful
    if res.status_code == 200:
        # Step 3: Create a ContentFile from the response content
        zip_content = ContentFile(res.content, name='my_file.zip')

        # Step 4: Save the ContentFile to the UploadedFile model
        uploaded_file_instance = UploadedFile()
        uploaded_file_instance.file.save('my_file.zip', zip_content, save=True)

        # Optionally, return the instance or perform further actions
        return uploaded_file_instance
    else:
        # Handle any errors
        raise Exception(f"Error fetching zip file: {res.status_code} - {res.text}")

# Call the function wherever appropriate in your application
