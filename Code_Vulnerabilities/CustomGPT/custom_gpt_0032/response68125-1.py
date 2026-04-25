
import requests
from django.http import JsonResponse

def check_file_exists(request):
    url = 'http://hostname/directory/file.jpg'  # Replace with your URL
    try:
        response = requests.head(url)  # Use HEAD to avoid downloading the file
        if response.status_code == 200:
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
