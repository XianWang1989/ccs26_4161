
import requests
import tempfile
import os
from django.core.files import File
from .models import UploadedFile  # Adjust the import based on your project structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_file:
        # Write the binary content to the temporary file
        temp_file.write(res.content)
        temp_file_path = temp_file.name  # Save the path for later use

    # Now, save the temporary file to your UploadedFile model
    with open(temp_file_path, 'rb') as f:
        uploaded_file = UploadedFile()
        uploaded_file.file.save(os.path.basename(temp_file_path), File(f))

    # Clean up the temporary file
    os.remove(temp_file_path)

    print("File saved successfully.")
else:
    print("Failed to retrieve the file:", res.status_code)
