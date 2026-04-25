
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust the import according to your app structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the request was successful
if res.status_code == 200:
    # Create an in-memory binary stream
    zip_file_data = BytesIO(res.content)

    # Create a ContentFile with the zip file content
    zip_file_content = ContentFile(zip_file_data.getvalue(), name='downloaded_file.zip')

    # Create the UploadedFile instance and save it
    my_file_instance = UploadedFile(file=zip_file_content)
    my_file_instance.save()
else:
    print(f"Error: {res.status_code}")
