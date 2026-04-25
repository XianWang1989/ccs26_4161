
import requests
import zipfile
from io import BytesIO
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust import according to your app structure

# Make the API request
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Ensure the response is successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_content = BytesIO(res.content)

    # Optionally, you can check if it's a valid zip file
    try:
        with zipfile.ZipFile(zip_content) as z:
            # List the contents of the zip file
            print(z.namelist())  # Prints names of files inside the zip

        # Now, create/upload the file in Django
        # You can save it directly to the UploadedFile model
        uploaded_file = UploadedFile()
        uploaded_file.file.save('my_file.zip', ContentFile(res.content), save=True)

        # Check if it was saved successfully
        print("File saved successfully!")

    except zipfile.BadZipFile:
        print("Received content is not a valid zip file.")
else:
    print(f"API call failed with status code: {res.status_code}")
