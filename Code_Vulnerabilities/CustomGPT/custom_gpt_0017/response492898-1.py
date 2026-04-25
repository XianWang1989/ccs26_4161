
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from your_app.models import UploadedFile  # Adjust the import according to your app structure
import io

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': open('path_to_your_file', 'rb')})

# Step 2: Check if the response is successful and get the content
if response.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = io.BytesIO(response.content)

    # Step 4: Create a Django File object
    django_file = File(zip_file, name='your_zip_file.zip')

    # Step 5: Create an instance of your UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('your_zip_file.zip', django_file)

    # Optionally, save the instance
    uploaded_file_instance.save()
else:
    print(f'Failed to download file: {response.status_code}')
