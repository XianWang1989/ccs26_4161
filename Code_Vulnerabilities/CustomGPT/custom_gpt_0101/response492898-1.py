
import requests
import zipfile
import io
from django.core.files.base import ContentFile
from your_app.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create a ZipFile object from the response content
    zip_file = zipfile.ZipFile(io.BytesIO(res.content))

    # Save the zip file to Django's FileField
    for file_info in zip_file.infolist():
        with zip_file.open(file_info) as file:
            uploaded_file = UploadedFile()
            uploaded_file.file.save(file_info.filename, ContentFile(file.read()))
            uploaded_file.save()
else:
    print("Failed to retrieve file:", res.status_code)
