
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = "http://example.com/api"  # Change with the actual target URL
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an error for bad responses
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
