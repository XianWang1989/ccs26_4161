
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.status_code == 200:
    # Create a ContentFile from the response content
    zip_file_content = ContentFile(res.content)

    # Create an instance of UploadedFile
    my_uploaded_file = UploadedFile()

    # Save the ContentFile to the FileField
    my_uploaded_file.file.save('myfile.zip', zip_file_content)

    # Don't forget to save the instance
    my_uploaded_file.save()
else:
    print(f"Failed to retrieve file: {res.status_code}")
