
    # Create a filename for the zip file
    zip_filename = 'your_zip_file.zip'  # You can customize the filename

    # Save the zip file using Django's storage system
    uploaded_file = UploadedFile()
    uploaded_file.file.save(zip_filename, ContentFile(zip_content))

    # Save the model instance
    uploaded_file.save()
else:
    print("Error: Unable to fetch the file from the API.")
