
import requests
from django.core.files.base import ContentFile
from myapp.models import UploadedFile  # Adjust the import as needed

# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the response is successful
if res.status_code == 200:
    # Create a ContentFile from the response content
    zip_content = ContentFile(res.content, name='myfile.zip')

    # Create an instance of your UploadedFile model
    uploaded_file = UploadedFile()
    uploaded_file.file.save('myfile.zip', zip_content)

    # Optional: Save the model instance if you need to
    uploaded_file.save()
else:
    print("Error:", res.status_code)
