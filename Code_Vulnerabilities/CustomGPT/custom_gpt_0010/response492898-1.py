
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile

# Step 1: Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful
if res.status_code == 200:
    # Step 3: Create an InMemoryUploadedFile instance
    zip_content = res.content  # Get the content as bytes
    zip_file = BytesIO(zip_content)  # Create a BytesIO object

    # Optional: Validate if the content is a valid zip
    try:
        with zipfile.ZipFile(zip_file) as z:
            z.testzip()  # Check for any errors in the zip file
    except zipfile.BadZipFile:
        print("Received content is not a valid zip file.")
        # Handle the error accordingly

    # Step 4: Create an UploadedFile instance
    my_file = InMemoryUploadedFile(
        file=zip_file,
        field_name='file',
        name='my_zip_file.zip',
        content_type='application/zip',
        size=len(zip_content),
        charset=None
    )

    # Step 5: Save it to the model
    uploaded_instance = UploadedFile()
    uploaded_instance.file.save('my_zip_file.zip', my_file)

    print("File uploaded successfully.")
else:
    print("Failed to retrieve the zip file from the API.")
