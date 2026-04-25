
from .models import UploadedFile  # Adjust import according to your project structure

# Create an instance of UploadedFile and save the content
uploaded_file = UploadedFile()
uploaded_file.file.save('my_zip_file.zip', ContentFile(zip_content))
uploaded_file.save()
