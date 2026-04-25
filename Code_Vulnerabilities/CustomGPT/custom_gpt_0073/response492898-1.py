
import requests
import tempfile
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from yourapp.models import UploadedFile

# Make the request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.ok:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        # Write the content to the temporary file
        tmp_file.write(response.content)
        tmp_file.flush()

        # Create an InMemoryUploadedFile instance
        with open(tmp_file.name, 'rb') as f:
            uploaded_file = InMemoryUploadedFile(
                f,
                None,
                'downloaded.zip',   # The desired name of the file
                'application/zip',   # MIME type
                f.tell(),            # Size of the file
                None
            )

        # Save the file to your UploadedFile model
        my_uploaded_file = UploadedFile(file=uploaded_file)
        my_uploaded_file.save()
