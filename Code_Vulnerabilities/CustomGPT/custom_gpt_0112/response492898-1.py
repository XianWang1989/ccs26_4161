
import requests
from django.core.files.base import ContentFile
from io import BytesIO
from zipfile import ZipFile
from yourapp.models import UploadedFile  # Adjust to your app name

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful and contains zip file
if res.status_code == 200 and res.headers['Content-Type'] == 'application/zip':
    zip_content = res.content  # Get the zip file content

    # Step 3: Create an in-memory file from the zip content
    zip_file = BytesIO(zip_content)

    # Optional: To check the contents of the zip file (for debugging)
    with ZipFile(zip_file) as zf:
        zf.printdir()  # Print the contents of the zip file

    # Step 4: Create a Django UploadedFile instance
    uploaded_file = UploadedFile()
    uploaded_file.file.save('your_filename.zip', ContentFile(zip_file.getvalue()))
    uploaded_file.save()

    print("Zip file successfully saved!")
else:
    print("Failed to retrieve the zip file.")
