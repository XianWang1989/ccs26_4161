
import requests
from django.http import JsonResponse

def check_file_exists(request):
    url = "http://hostname/directory/file.jpg"

    try:
        response = requests.head(url)
        if response.status_code == 200:
            return JsonResponse({"exists": True})
        else:
            return JsonResponse({"exists": False})
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)})
