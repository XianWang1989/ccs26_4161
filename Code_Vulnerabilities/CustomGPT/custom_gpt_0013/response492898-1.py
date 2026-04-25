
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Make the API call to get the zip file
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Getting the content of the response
    zip_content = response.content

    # Create a ContentFile from the response content
    zip_file = ContentFile(zip_content)

    # Specify the name for the new file
    filename = 'my_archive.zip'

    # Save the ContentFile to the Django model
    my_uploaded_file = UploadedFile()
    my_uploaded_file.file.save(filename, zip_file)

    # Optionally save the model instance if required
    my_uploaded_file.save()

else:
    print(f"Error: {response.status_code}")
