
import requests
import zipfile
import io
from django.core.files.base import ContentFile
from django.core.files import File
from your_app.models import UploadedFile  # Update with your actual app name

def save_zip_from_api():
    # Make the API call
    res = requests.post('http://url/to/api', files={'file_pro': my_file})

    # Check if the response is successful
    if res.status_code == 200:
        # Create a BytesIO object from the response content
        zip_content = io.BytesIO(res.content)

        # Open the ZIP file
        with zipfile.ZipFile(zip_content) as z:
            # Optionally, you can inspect the contents of the ZIP file here
            # For example: print(z.namelist())

            # Save each file in the ZIP to your Django model
            for file_name in z.namelist():
                with z.open(file_name) as file:
                    # Read the content of the file
                    file_data = file.read()
                    # Create a ContentFile from the file data
                    content_file = ContentFile(file_data, name=file_name)

                    # Create a new UploadedFile instance and save it
                    uploaded_file = UploadedFile(file=content_file)
                    uploaded_file.save()

        print("Files saved successfully.")

    else:
        print("Failed to retrieve the ZIP file:", res.status_code)

# Call the function to execute
save_zip_from_api()
