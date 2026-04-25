
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import zipfile
import io

# Make the API call to get the zip file
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

# Check if the response is ok
if res.status_code == 200:
    # Create a BytesIO object to read the content
    zip_file = io.BytesIO(res.content)

    # Optional: Confirm if the content is indeed a zip file
    with zipfile.ZipFile(zip_file, 'r') as z:
        print(z.namelist())  # This will list the contents of the zip file

    # Save it as an UploadedFile in Django
    my_file = InMemoryUploadedFile(
        file=zip_file, 
        field_name=None, 
        name='my_downloaded_file.zip', 
        content_type='application/zip', 
        size=res.content.__sizeof__(), 
        charset=None
    )

    # Assuming you have an instance of UploadedFile model
    uploaded_file_instance = UploadedFile()
    uploaded_file_instance.file.save(my_file.name, ContentFile(res.content), save=True)

else:
    print("Failed to retrieve the zip file. Status code:", res.status_code)
