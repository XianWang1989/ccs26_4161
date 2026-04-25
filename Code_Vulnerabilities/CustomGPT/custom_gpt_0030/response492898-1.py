
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
import zipfile

# Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Optionally verify its a zip file
    with zipfile.ZipFile(zip_file) as my_zip:
        # Optionally, list files or perform other operations
        print(my_zip.namelist())

    # Now, create a Django FileField compatible file
    my_file_field = ContentFile(response.content, name='my_downloaded_file.zip')

    # Save to your UploadedFile instance
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('my_downloaded_file.zip', my_file_field)

    # Don't forget to save the model instance
    uploaded_file_instance.save()
else:
    print(f"Failed to retrieve ZIP file: {response.status_code}")
