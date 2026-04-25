
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile  # Adjust the import depending on your app structure

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful and the content type is zip
if res.status_code == 200 and res.headers['Content-Type'] == 'application/zip':
    # Create a ContentFile from the response content (binary)
    zip_content = ContentFile(res.content)

    # Create an instance of UploadedFile
    my_uploaded_file = UploadedFile()

    # Saving the content to the FileField
    my_uploaded_file.file.save('filename.zip', zip_content)

    # Save the instance to the database
    my_uploaded_file.save()
else:
    # Handle the case where response is not successful
    print("Failed to retrieve the zip file. Status code:", res.status_code)
