
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from zipfile import ZipFile

# Your API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.ok:  # Check if the request was successful
    # Create a BytesIO object from the response content
    zip_bytes = BytesIO(res.content)

    # Optionally, you can check the content type if you want to ensure it's a zip file
    if res.headers['Content-Type'] == 'application/zip':
        # Create the UploadedFile instance
        my_file = UploadedFile()

        # Create a ContentFile from the BytesIO object and assign it to the file field
        my_file.file.save('downloaded_file.zip', ContentFile(zip_bytes.getvalue()), save=False)

        # Save the instance
        my_file.save()
        print("File saved successfully!")
    else:
        print("The response is not a zip file.")
else:
    print("Failed to retrieve the zip file:", res.status_code)
