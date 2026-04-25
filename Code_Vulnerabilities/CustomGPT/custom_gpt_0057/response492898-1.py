
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from myapp.models import UploadedFile

def save_zip_from_api():
    res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

    if res.status_code == 200:
        zip_content = res.content
        file_name = 'myfile.zip'  # Name your file appropriately

        # Save to UploadedFile model
        uploaded_file = UploadedFile()
        uploaded_file.file.save(file_name, ContentFile(zip_content), save=True)

        print(f'Successfully saved the zip file as {uploaded_file.file.name}')
    else:
        print(f'Error: Received status code {res.status_code}')

save_zip_from_api()
