
import requests
import zipfile
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile  # Adjust the import according to your app structure

# Make the POST request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the request was successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Optionally, you can verify the content is a zip file
    with zipfile.ZipFile(zip_file) as z:
        # Extracting or inspecting files is optional
        # For example:
        print(z.namelist())  # List contents of the zip

    # Save the zip file to your UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('filename.zip', ContentFile(res.content))

    # Save the model instance if needed
    uploaded_file_instance.save()

else:
    print(f"Request failed with status code: {res.status_code}")
