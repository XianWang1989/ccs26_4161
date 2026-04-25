
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import zipfile
import io

# Step 1: Make the POST request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check for a successful response
if res.status_code == 200:
    # Step 3: Load the zip file from the response content
    zip_file = io.BytesIO(res.content)

    # Step 4: Create a ZIPFile object to verify its contents (optional)
    with zipfile.ZipFile(zip_file) as my_zip:
        # If needed, list files in the zip (optional)
        print(my_zip.namelist())

    # Step 5: Create an InMemoryUploadedFile
    my_file = InMemoryUploadedFile(
        file=zip_file,
        field_name=None,
        name='my_zip_file.zip',
        content_type='application/zip',
        size=res.content.__sizeof__(),
        charset=None
    )

    # Step 6: Save the file using your UploadedFile model
    uploaded_file_instance = UploadedFile(file=my_file)
    uploaded_file_instance.save()
else:
    print(f"Error: {res.status_code} - {res.text}")
