
import requests
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from myapp.models import UploadedFile

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Ensure the request was successful
if res.status_code == 200:
    # Create a temporary file
    with NamedTemporaryFile(delete=False) as temp_file:
        # Write the response content (zip file) to the temporary file
        temp_file.write(res.content)
        temp_file_path = temp_file.name  # Get the file path

    # Create an UploadedFile instance and save it
    uploaded_file_instance = UploadedFile()
    with open(temp_file_path, 'rb') as f:
        uploaded_file_instance.file.save('downloaded_file.zip', ContentFile(f.read()))

    uploaded_file_instance.save()

    # Optionally delete the temporary file if not needed
    # os.unlink(temp_file_path)

else:
    print("Failed to retrieve the ZIP file, status code:", res.status_code)
