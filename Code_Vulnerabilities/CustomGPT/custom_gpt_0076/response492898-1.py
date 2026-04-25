
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from io import BytesIO
import zipfile

# Step 1: Make the API call
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Step 3: Optionally, check the zip file contents
    with zipfile.ZipFile(zip_file, 'r') as z:
        print(z.namelist())  # List the names of the files in the zip, if needed

    # Step 4: Save the zip file to Django FileField
    uploaded_file_name = 'filename.zip'  # Adjust the filename as needed
    file_storage_path = default_storage.save(uploaded_file_name, ContentFile(response.content))

    # Step 5: Create an instance of your UploadedFile model
    uploaded_file_instance = UploadedFile(file=file_storage_path)
    uploaded_file_instance.save()

    print("File uploaded successfully.")
else:
    print("Failed to retrieve the zip file. Status code:", response.status_code)
