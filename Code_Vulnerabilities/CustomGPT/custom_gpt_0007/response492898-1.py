
import requests
from django.core.files.base import ContentFile
from django.core.files import File
from io import BytesIO
import zipfile

# Step 1: Make the API request to get the zip file.
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Step 2: Check if the response is successful.
if res.status_code == 200:
    # Step 3: Create a BytesIO object from the response content.
    zip_file = BytesIO(res.content)

    # Step 4: Open the zip file using zipfile module
    with zipfile.ZipFile(zip_file, 'r') as z:
        # Optional: List contents of the zip
        print(z.namelist())

        # Step 5: Save the entire zip or just a specific file in it
        # You can either save the whole zip or extract a specific file
        # For saving the whole zip file:
        my_uploaded_file = UploadedFile()
        my_uploaded_file.file.save('my_downloaded_file.zip', ContentFile(res.content))

        # If you want to extract a specific file from the zip and save it
        # for file_name in z.namelist():
        #     with z.open(file_name) as file:
        #         my_uploaded_file.file.save(file_name, ContentFile(file.read()))
else:
    print("Failed to download the zip file. Status Code:", res.status_code)
