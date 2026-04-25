
import requests
from django.core.files.base import ContentFile
from your_app.models import UploadedFile  # Update with your actual app name

# Make request to the API
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if res.status_code == 200:
    # Create an UploadedFile instance
    new_file = UploadedFile()

    # Wrap the response content in ContentFile
    content_file = ContentFile(res.content)

    # Save the content to the FileField
    new_file.file.save('your_zip_file.zip', content_file)  # The filename can be adjusted as needed
    new_file.save()  # Save the UploadedFile instance

    print("File uploaded successfully!")
else:
    print("Failed to fetch file from API. Status code:", res.status_code)
