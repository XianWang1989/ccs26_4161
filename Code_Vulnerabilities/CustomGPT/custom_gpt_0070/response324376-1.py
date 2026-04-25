
import requests
from django.http import JsonResponse

def send_post_request():
    try:
        response = requests.post('http://external.server/endpoint', data={'key': 'value'})
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
