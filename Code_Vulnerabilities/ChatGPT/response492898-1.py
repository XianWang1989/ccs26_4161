
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Adjust the import to your app structure

# Make the API call to get the zip file
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Prepare a Django FileField-compatible content
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_zip_file.zip')

    # Create and save the uploaded file instance
    uploaded_file_instance = UploadedFile(file=content_file)
    uploaded_file_instance.save()
else:
    print(f"Error: Received a {res.status_code} status code from the API.")
