
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from myapp.models import UploadedFile  # Adjust the import based on your app structure

# Step 1: Make the API call
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Step 2: Validate the response
if res.status_code == 200:
    # Step 3: Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # Step 4: Create an InMemoryUploadedFile
    uploaded_file = InMemoryUploadedFile(
        file=zip_file,
        field_name=None,
        name='downloaded_file.zip',  # Name of the file
        content_type='application/zip',
        size=res.content.__sizeof__(),
        charset=None
    )

    # Step 5: Create the model instance and save
    uploaded_instance = UploadedFile(file=uploaded_file)
    uploaded_instance.save()
else:
    print("Error: ", res.status_code)
