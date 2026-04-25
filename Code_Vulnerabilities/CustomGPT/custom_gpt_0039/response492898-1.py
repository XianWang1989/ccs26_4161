
import requests
import zipfile
import io
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

# Make the POST request to the API
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if res.ok:
    # Read the content of the response (zip file)
    zip_content = res.content

    # Create a BytesIO object from the zip content
    zip_io = io.BytesIO(zip_content)

    # Optionally, to verify if it's a valid zip file
    try:
        with zipfile.ZipFile(zip_io, 'r') as zip_file:
            # This will raise an exception if the file is not a zip
            zip_file.testzip()  # Check if zip is valid

            # Save the zip file into the Django model
            uploaded_file = UploadedFile()
            uploaded_file.file.save('filename.zip', ContentFile(zip_content))
            uploaded_file.save()
            print("Zip file saved successfully.")
    except zipfile.BadZipFile:
        print("The content is not a valid zip file.")
else:
    print(f"Request failed with status code: {res.status_code}")
