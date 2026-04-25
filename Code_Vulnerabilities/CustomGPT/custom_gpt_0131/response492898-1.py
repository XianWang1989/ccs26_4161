
import requests
import zipfile
import io
from django.core.files.base import ContentFile

# Call the API to get the zip file response
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is successful
if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = io.BytesIO(res.content)

    # Use the zipfile module to extract the contents if needed
    with zipfile.ZipFile(zip_file_content) as z:
        # If you want to save it to the model directly,
        # you can iterate over the contents of the zip file if needed
        for file_info in z.infolist():
            # Assuming you want to save the first file in the zip
            with z.open(file_info) as file:
                # Read the content of the file
                file_content = file.read()

                # Create an UploadedFile instance with the content
                my_file = UploadedFile(
                    file=ContentFile(file_content, name=file_info.filename)
                )
                my_file.save()

else:
    print(f"Error: Received response with status code {res.status_code}")
