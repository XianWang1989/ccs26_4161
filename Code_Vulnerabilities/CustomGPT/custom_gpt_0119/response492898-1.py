
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from zipfile import ZipFile
from your_app.models import UploadedFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check for a successful response
if res.status_code == 200:
    # Create a file-like object from the response content
    zip_file = BytesIO(res.content)

    # Optionally, check if the content is zip
    with ZipFile(zip_file) as my_zip:
        # Optionally list contents or perform actions
        print(my_zip.namelist())  # List files in the zip

    # Create an InMemoryUploadedFile
    uploaded_file = InMemoryUploadedFile(
        file=zip_file,
        field_name='file_field', # replace with your actual field name
        name='downloaded_file.zip',
        content_type='application/zip',
        size=res.content.__sizeof__(),
        charset=None
    )

    # Save to your model
    uploaded_instance = UploadedFile(file=uploaded_file)
    uploaded_instance.save()
else:
    print("Error fetching file:", res.status_code)
