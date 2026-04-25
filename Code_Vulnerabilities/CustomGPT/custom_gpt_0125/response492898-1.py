
import requests
import zipfile
import io
from django.core.files.base import ContentFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Assuming the response content is the zip file in bytes
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_content = io.BytesIO(res.content)

    # Verify it is indeed a zip file
    with zipfile.ZipFile(zip_content, 'r') as z:
        # Iterate through the files in the zip
        for filename in z.namelist():
            # Optionally extract or process files here

            # Example: Save the first file to Django's UploadedFile model
            file_data = z.read(filename)
            my_uploaded_file = UploadedFile()
            my_uploaded_file.file.save(filename, ContentFile(file_data), save=True)
