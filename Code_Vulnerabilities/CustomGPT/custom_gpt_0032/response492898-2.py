
import zipfile
import io
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust import based on your app structure

# Assuming 'zip_content' contains the binary data from the response
if zip_content:
    # Use BytesIO to read the zip data
    zip_file = io.BytesIO(zip_content)

    # Optionally, you could validate the zip file (not mandatory)
    with zipfile.ZipFile(zip_file, 'r') as z:
        # List contents or perform checks if needed
        z.testzip()  # This will raise an error if the zip is corrupt.

    # Create a Django UploadedFile instance
    uploaded_file = UploadedFile()

    # Create ContentFile with the zip content
    uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_content))
    uploaded_file.save()
