
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = 'https://api.example.com/endpoint'
    data = {'key': 'value'}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse(response.json())
    except requests.ConnectionError as e:
        return JsonResponse({'error': str(e)}, status=500)
