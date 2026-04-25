
import requests
from django.core.files.base import ContentFile
from your_app.models import UploadedFile

# Step 1: Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

if response.status_code == 200:
    # Step 2: Save the zip file to the Django model
    # Get the byte content of the zip file
    zip_content = response.content

    # Create a ContentFile from the response content
    content_file = ContentFile(zip_content)

    # Step 3: Save the file in your UploadedFile model
    my_uploaded_file = UploadedFile()
    my_uploaded_file.file.save('my_zip_file.zip', content_file)  # Provide a file name as needed
    my_uploaded_file.save()  # Save the model instance
else:
    print("Error occurred:", response.status_code, response.text)
