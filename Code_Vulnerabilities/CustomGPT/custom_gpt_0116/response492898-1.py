
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from io import BytesIO
import zipfile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the request was successful
if res.status_code == 200:
    # Read the response content
    zip_content = res.content  # This is the raw zip file content

    # Create a BytesIO object from the content
    zip_file = BytesIO(zip_content)

    # Optionally, you can validate the zip file
    try:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            # List files in the archive (optional check)
            print(zf.namelist())
    except zipfile.BadZipFile:
        print("Received content is not a valid zip file.")

    # Save the zip file using UploadedFile model
    uploaded_file = UploadedFile()  # Create an instance of your model
    uploaded_file.file.save('my_uploaded_zip.zip', ContentFile(zip_content))
    uploaded_file.save()  # Save the instance to the database
else:
    print(f"Error: {res.status_code}, {res.text}")
