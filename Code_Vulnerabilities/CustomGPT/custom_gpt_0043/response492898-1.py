
import requests
from django.core.files import File
from django.core.files.base import ContentFile
from django.http import HttpResponse
from io import BytesIO
from .models import UploadedFile

def upload_zip_view(request):
    if request.method == 'POST':
        # Replace with your actual URL and parameters
        res = requests.post('http://url/to/api', files={'file_pro': request.FILES['file']})

        if res.status_code == 200:
            # Create a BytesIO stream from the response content
            zip_file_stream = BytesIO(res.content)

            # Create a new UploadedFile instance and save it
            uploaded_file = UploadedFile()
            uploaded_file.file.save('my_file.zip', ContentFile(zip_file_stream.getvalue()), save=True)

            return HttpResponse('File saved successfully!')
        else:
            return HttpResponse('Failed to retrieve zip file')
    return HttpResponse('Invalid request method')
