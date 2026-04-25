
# Make the API request
response = requests.post('http://url/to/api', files={'file_pro': my_file})

# Check if the request was successful
if response.status_code == 200:
    # Read the content of the response (zip file)
    zip_content = response.content

    # Create a BytesIO stream from the zip content
    zip_file_stream = BytesIO(zip_content)

    # Use zipfile to handle the zip file
    with zipfile.ZipFile(zip_file_stream) as zf:
        # Here you can check the contents of the zip file if needed
        # For example, listing the files
        file_list = zf.namelist()
        print("Files in zip:", file_list)

        # Optionally read files from the zip
        # For example, to read the first file in the zip
        first_file_name = file_list[0]
        with zf.open(first_file_name) as first_file:
            file_data = first_file.read()
            # You can convert this to an InMemoryUploadedFile
            uploaded_file = InMemoryUploadedFile(
                file=ContentFile(file_data),
                field_name=None,
                name=first_file_name,
                content_type='application/zip',
                size=len(file_data),
                charset=None
            )

            # Now save it to your UploadedFile model
            uploaded_instance = UploadedFile(file=uploaded_file)
            uploaded_instance.save()
else:
    print("Failed to retrieve the file: ", response.status_code)
