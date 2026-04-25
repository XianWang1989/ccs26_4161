import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # replace with your actual model import

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check the response
if res.status_code == 200:
    # Create an instance of your model
    uploaded_file = UploadedFile()

    # Use ContentFile to wrap the binary content
    zip_content = ContentFile(res.content)

    # Save to the FileField (give it a name)
    uploaded_file.file.save('downloaded.zip', zip_content)
    uploaded_file.save()
