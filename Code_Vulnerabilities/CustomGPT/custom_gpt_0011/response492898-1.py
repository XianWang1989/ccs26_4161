
import requests
import zipfile
from io import BytesIO
from django.core.files.base import ContentFile

# Make the request to the API
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Use BytesIO to handle the response content
    zip_file = BytesIO(res.content)

    # Open the zip file using the zipfile module
    with zipfile.ZipFile(zip_file) as z:
        # Optionally, list the contents of the zip file
        print(z.namelist())

        # Read the content of the zip file if needed
        # Example: Reading a specific file (replace 'example.txt' with your file)
        file_content = z.read('example.txt')

        # Create the UploadedFile instance
        my_file = ContentFile(file_content, name='myfile.zip')

        # Save the file to UploadedFile model
        uploaded_file_instance = UploadedFile(file=my_file)
        uploaded_file_instance.save()
else:
    print(f"Error: {res.status_code} - {res.content}")
