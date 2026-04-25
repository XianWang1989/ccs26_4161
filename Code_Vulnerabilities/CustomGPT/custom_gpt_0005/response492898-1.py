
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

if res.status_code == 200:
    # Get the content of the response
    zip_content = res.content

    # Create a ContentFile from the zip content
    zip_file = ContentFile(zip_content)

    # Create an instance of UploadedFile
    uploaded_file_instance = UploadedFile()

    # Save the zip file to the FileField
    uploaded_file_instance.file.save('my_zip_file.zip', zip_file)

    # Now the uploaded_file_instance is saved in the database
    uploaded_file_instance.save()
else:
    print("Failed to retrieve the zip file.")
