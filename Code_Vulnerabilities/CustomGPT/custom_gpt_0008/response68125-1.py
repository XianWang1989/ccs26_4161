
import requests
from django.http import JsonResponse

def check_file_exists(request):
    file_url = 'http://hostname/directory/file.jpg'
    try:
        response = requests.head(file_url)
        # Check if response status code indicates the file exists
        if response.status_code == 200:
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
    except requests.exceptions.RequestException as e:
        # Handle any errors (e.g., connection issues)
        return JsonResponse({'error': str(e)}, status=500)
