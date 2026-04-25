
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
import zipfile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the response is successful
if res.status_code == 200:
    # Create a BytesIO stream from response content
    zip_stream = BytesIO(res.content)

    # Open the zip file
    with zipfile.ZipFile(zip_stream) as my_zip:
        # Extract the content or save directly
        for file_info in my_zip.infolist():
            # Read the file content
            with my_zip.open(file_info) as extracted_file:
                file_content = extracted_file.read()

                # Create a Django-compatible file
                my_file = ContentFile(file_content, name=file_info.filename)
                uploaded_file_instance = UploadedFile(file=my_file)
                uploaded_file_instance.save()

    print("Zip file processed and saved.")
else:
    print("Failed to fetch the ZIP file.")
