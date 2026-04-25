
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = 'https://external-server.com/api/endpoint'
    data = {'key': 'value'}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
