
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from your_app.models import UploadedFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response was successful
if res.status_code == 200:
    # Assuming the content is the zip file binary data
    zip_content = res.content

    # Create a BytesIO object from the content
    zip_file = BytesIO(zip_content)

    # Create a ContentFile from the BytesIO
    content_file = ContentFile(zip_file.getvalue(), name='downloaded_file.zip')

    # Save it to the UploadedFile model
    new_file = UploadedFile(file=content_file)
    new_file.save()
else:
    print("Failed to download zip file:", res.status_code)
