
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
from zipfile import ZipFile

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Ensure we have a successful response
if res.status_code == 200:
    # Use BytesIO to open the content as a file
    zip_data = BytesIO(res.content)

    # Optional: Validate the zip file
    try:
        with ZipFile(zip_data) as zip_file:
            # You can check the contents, if necessary
            zip_file.testzip()  # This will raise an error if not a valid zip
    except (zipfile.BadZipFile, KeyError) as e:
        print(f"Error validating zip file: {e}")
        # Handle the error as appropriate
    else:
        # When you are sure it's a valid zip, save it to your model
        zip_data.seek(0)  # Go to the beginning of the BytesIO object
        my_file = ContentFile(zip_data.read(), name='my_uploaded_zip.zip')

        # Now create or save your UploadedFile instance
        uploaded_file_instance = UploadedFile(file=my_file)
        uploaded_file_instance.save()

        print("Zip file saved successfully!")
else:
    print(f"Request failed with status code: {res.status_code}")
