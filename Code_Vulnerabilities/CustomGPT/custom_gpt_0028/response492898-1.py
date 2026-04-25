
import requests
from django.core.files.base import ContentFile
from yourapp.models import UploadedFile

def save_zip_file_to_model(api_url, file_data):
    # Make the API request
    res = requests.post(api_url, files={'file_pro': file_data})

    # Check if the request was successful
    if res.status_code == 200:
        # Create a ContentFile from the response content
        zip_content = ContentFile(res.content, name='downloaded_file.zip')

        # Create an instance of UploadedFile and save it
        uploaded_file = UploadedFile(file=zip_content)
        uploaded_file.save()
        return uploaded_file
    else:
        raise Exception(f"API request failed with status code {res.status_code}")

# Usage Example
# my_file is the data you want to send in the request
# uploaded_file_instance = save_zip_file_to_model('http://url/to/api', my_file)
