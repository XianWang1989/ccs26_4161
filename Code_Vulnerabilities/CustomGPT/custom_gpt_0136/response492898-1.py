
import requests
from django.core.files.base import ContentFile
from django.db import models

# Your Django model
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=255)

# Function to save API response as a zip file
def save_zip_from_api():
    # Make the API call
    res = requests.post('http://url/to/api', files={'file_pro': open('path_to_your_file', 'rb')})

    # Ensure the request was successful
    if res.status_code == 200:
        # Create UploadedFile instance
        uploaded_file = UploadedFile()
        # Save the zip content to the FileField
        uploaded_file.file.save('response.zip', ContentFile(res.content))
        uploaded_file.save()

        print("Zip file saved successfully.")
    else:
        print("Failed to retrieve zip file:", res.status_code)

# Call the function
save_zip_from_api()
