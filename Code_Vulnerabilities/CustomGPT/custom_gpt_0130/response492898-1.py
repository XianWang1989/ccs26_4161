
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Ensure the request was successful
if res.status_code == 200:
    # Step 2: Create a BytesIO object
    zip_file = BytesIO(res.content)

    # Optionally, check if it's a valid zip file
    with zipfile.ZipFile(zip_file) as z:
        z.testzip()  # Raises a BadZipFile exception if not valid

    # Step 3: Create a Django UploadedFile
    uploaded_file = InMemoryUploadedFile(
        zip_file,
        None,
        'filename.zip',  # Name of the file
        'application/zip',  # Content type
        zip_file.getbuffer().nbytes,
        None
    )

    # Step 4: Save it to your model
    my_uploaded_file = UploadedFile(file=uploaded_file)
    my_uploaded_file.save()
