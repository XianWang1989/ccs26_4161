
import requests
import zipfile
import io
from django.core.files.base import ContentFile
from myapp.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.ok:  # Check if the response was successful
    # Create a BytesIO object from the response content
    zip_file = io.BytesIO(res.content)

    # Use zipfile to read the contents if needed (optional step)
    with zipfile.ZipFile(zip_file) as zf:
        # List contents of the zip (optional)
        print(zf.namelist())

    # Save the ZIP file to your UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('myfile.zip', ContentFile(res.content))
    uploaded_file.save()

    print("File saved successfully!")
else:
    print("Failed to retrieve file from API.")
