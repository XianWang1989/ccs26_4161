
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust the import based on your project structure

def save_zip_from_api(my_file):
    # Make API call
    response = requests.post('http://url/to/api', files={'file_pro': my_file})

    # Check response status
    if response.status_code == 200:
        # Get the byte content of the zip file
        zip_content = response.content

        # Create a filename for the zip file
        zip_filename = 'your_zip_file.zip'

        # Save the zip file to the UploadedFile model
        uploaded_file = UploadedFile()
        uploaded_file.file.save(zip_filename, ContentFile(zip_content))

        # Save the instance
        uploaded_file.save()
    else:
        print("Error: Unable to fetch the file from the API.")
