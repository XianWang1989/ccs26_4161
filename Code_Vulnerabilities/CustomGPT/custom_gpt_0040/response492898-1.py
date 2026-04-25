
import requests
import zipfile
import io
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call and get the response
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check for a successful response
if res.status_code == 200:
    # Step 3: Use BytesIO to handle the binary content
    zip_content = io.BytesIO(res.content)

    # Step 4: Optionally, you can validate the zip file
    with zipfile.ZipFile(zip_content, 'r') as zip_file:
        # List contents or perform any other checks if needed
        print(zip_file.namelist())  # List the contents of the zip file

    # Step 5: Prepare to save it as an UploadedFile
    file_name = 'uploaded_file.zip'  # You can customize the file name
    uploaded_file = UploadedFile(file=ContentFile(res.content, name=file_name))
    uploaded_file.save()
else:
    print('Failed to retrieve zip file, status code:', res.status_code)
