
import requests
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import zipfile

# Make the API call and get the zip file content
res = requests.post('http://url/to/api', files={'file_pro': *my_file*})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file_content = BytesIO(res.content)

    # Open the zip file to ensure we have a proper zip structure
    try:
        with zipfile.ZipFile(zip_file_content) as z:
            # Check the contents of the zip file (optional)
            print(z.namelist())

            # To save the zip file, you want to create an UploadedFile instance
            z.seek(0)  # Go back to the start of the BytesIO stream
            uploaded_file = InMemoryUploadedFile(
                file=zip_file_content,
                field_name=None,
                name='myfile.zip',  # Use a desired name for the saved file
                content_type='application/zip',
                size=res.headers.get('Content-Length', len(res.content)),
                charset=None
            )

            # Save the uploaded file in the UploadedFile model
            my_uploaded_file_instance = UploadedFile(file=uploaded_file)
            my_uploaded_file_instance.save()
            print("File saved successfully!")

    except zipfile.BadZipFile:
        print("The response content is not a valid zip file.")
else:
    print("Failed to retrieve the zip file:", res.status_code)
