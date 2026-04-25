
import requests
from django.core.files.base import ContentFile
from io import BytesIO
import zipfile

# Make the request to the API
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the request was successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = BytesIO(response.content)

    # Optionally, you can check if it's indeed a zip file
    with zipfile.ZipFile(zip_file_content) as z:
        # List the contents of the zip file (optional)
        print(z.namelist())

    # Now save it as an UploadedFile instance
    uploaded_file = UploadedFile()
    uploaded_file.file.save('my_file.zip', ContentFile(response.content))
    uploaded_file.save()
else:
    print("Failed to retrieve the zip file. Status code:", response.status_code)
