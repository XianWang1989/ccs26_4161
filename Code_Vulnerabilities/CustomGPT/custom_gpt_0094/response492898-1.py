
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Step 1: Make the API call to get the zip file
response = requests.post('http://url/to/api', files={'file_pro': my_file})
if response.status_code == 200:
    zip_content = response.content  # This holds the binary content of the zip file

    # Step 2: Create a BytesIO object from the response content
    zip_file = BytesIO(zip_content)

    # Step 3: Save the zip file to the Django model
    my_file = UploadedFile()
    my_file.file.save('my_zip_file.zip', ContentFile(zip_file.getvalue()))  # Save with a name and content
    my_file.save()  # Save the model instance

    print("Zip file saved successfully!")
else:
    print("Failed to retrieve the zip file, status code:", response.status_code)
