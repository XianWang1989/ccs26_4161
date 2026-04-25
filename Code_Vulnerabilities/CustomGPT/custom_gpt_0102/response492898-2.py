
# Make the API call
res = requests.post('http://url/to/api', files={'file_pro': 'your_file_here'})

if res.status_code == 200:
    # Create a BytesIO object from the response content
    zip_file = BytesIO(res.content)

    # You can also verify the content type if needed
    # if 'application/zip' in res.headers.get('Content-Type', ''):

    # Optionally, extract files from the zip if needed
    with ZipFile(zip_file) as z:
        # Example: Extract a specific file's content
        # file_name = z.namelist()[0]  # Get the first file name
        # file_content = z.read(file_name)  # Read its content

        # For now, we will save the zip file directly
        zip_file.seek(0)  # Reset pointer to the beginning

        # Create a Django FileField object to save
        filename = 'uploaded_file.zip'  # or any naming convention
        file_content = ContentFile(zip_file.read(), name=filename)

        # Save to your UploadedFile model
        uploaded_file = UploadedFile(file=file_content)
        uploaded_file.save()
else:
    print("Failed to retrieve the file.")
