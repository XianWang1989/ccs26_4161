
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from .models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Create the UploadedFile instance
    uploaded_file = UploadedFile()

    # Use ContentFile to save the BytesIO content
    uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_file.getvalue()))

    # Optionally save the instance if you need to
    uploaded_file.save()
else:
    print('Request failed with status code:', res.status_code)
