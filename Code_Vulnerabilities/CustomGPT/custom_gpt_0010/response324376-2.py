
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = 'http://external-server/api'
    data = {'key': 'value'}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Will raise an HTTPError if the response was unsuccessful
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
