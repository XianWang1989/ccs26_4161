
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = "http://external-server/api"
    data = {'key': 'value'}

    try:
        response = requests.post(url, json=data, timeout=5)
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.exceptions.ConnectionError as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
