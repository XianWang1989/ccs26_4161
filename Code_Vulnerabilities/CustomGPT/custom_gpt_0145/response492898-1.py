
import requests
from io import BytesIO
from django.core.files import File
from your_app.models import UploadedFile

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': 'my_file'})

# Step 2: Check for a successful response
if response.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Step 4: Create an instance of the UploadedFile model
    my_file = UploadedFile()

    # Step 5: Save the zip file to the file field
    my_file.file.save('filename.zip', File(zip_file), save=True)

    print("File saved successfully!")
else:
    print("Failed to retrieve the zip file. Status code:", response.status_code)
