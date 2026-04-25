
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Check if the response is successful
if res.status_code == 200:
    # Step 3: Create a ContentFile from the response content
    zip_file_content = ContentFile(res.content, name='downloaded_file.zip')

    # Step 4: Create an instance of the UploadedFile model
    uploaded_file_instance = UploadedFile()

    # Step 5: Assign the file to the FileField
    uploaded_file_instance.file.save('downloaded_file.zip', zip_file_content, save=True)

    # Now, uploaded_file_instance is saved with the zip file in the FileField

else:
    # Handle the error
    print("Error:", res.status_code)
