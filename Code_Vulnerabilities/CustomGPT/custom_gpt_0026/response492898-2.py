
# Make the API call
url = 'http://url/to/api'
res = requests.post(url, files={'file_pro': my_file})

# Check if the response is successful
if res.status_code == 200:
    # Create an in-memory bytes buffer
    zip_file_bytes = io.BytesIO(res.content)

    # Check if the content is a zip file
    if zipfile.is_zipfile(zip_file_bytes):
        # Use the zipfile module to extract or read the contents if necessary
        with zipfile.ZipFile(zip_file_bytes, 'r') as zip_ref:
            # You can extract files or read specific files here
            # For example, let's read a specific file from the zip
            file_name = zip_ref.namelist()[0]  # get the first file name
            file_data = zip_ref.read(file_name)  # read its content

            # Create the UploadedFile instance
            uploaded_file = InMemoryUploadedFile(
                file=ContentFile(file_data),
                field_name='file',
                name=file_name,  # name to save the file as
                content_type='application/zip',  # appropriate content type
                size=len(file_data),
                charset=None
            )

            # Saving the instance to your model
            my_uploaded_file = UploadedFile(file=uploaded_file)
            my_uploaded_file.save()
    else:
        print("Response is not a valid zip file.")
else:
    print(f"Error: {res.status_code}")
