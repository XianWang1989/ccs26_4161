
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# Make the API call
response = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if response.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(response.content)

    # Create an UploadedFile instance
    my_uploaded_file = InMemoryUploadedFile(
        zip_file,
        None,
        'downloaded.zip',  # Give your file a name
        'application/zip',
        zip_file.getbuffer().nbytes,
        None
    )

    # Save it to your model (assuming you have an instance of UploadedFile)
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save('downloaded.zip', my_uploaded_file)

    # Optionally save the instance if needed
    uploaded_file_instance.save()
else:
    print(f"Failed to retrieve file: {response.status_code}")
