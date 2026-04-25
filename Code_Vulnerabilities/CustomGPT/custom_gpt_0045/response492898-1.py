
import requests
import tempfile
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from myapp.models import UploadedFile  # Replace 'myapp' with your actual app name

def upload_zip_file():
    # Make a POST request to the API to receive the zip file
    response = requests.post('http://url/to/api', files={'file_pro': my_file})

    if response.status_code == 200:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_file:
            # Write the response content to the temporary file
            temp_file.write(response.content)
            temp_file_path = temp_file.name  # Get the path of the temporary file

        # Open the temporary file and save it to the UploadedFile model
        with open(temp_file_path, 'rb') as file:
            # Create an instance of UploadedFile, binding the file to the file field
            uploaded_file = UploadedFile(file=File(file, name='uploaded_file.zip'))
            uploaded_file.save()

        print("File uploaded successfully.")

    else:
        print(f"Failed to retrieve zip file. Status code: {response.status_code}")
