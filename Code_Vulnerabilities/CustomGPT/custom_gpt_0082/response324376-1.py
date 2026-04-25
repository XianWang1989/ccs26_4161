
import requests
from django.http import JsonResponse

def send_post_request(request):
    url = 'https://external-server.com/api'
    payload = {'key': 'value'}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.ConnectionError as e:
        # Log the error for debugging
        print(f"ConnectionError: {e}")
        return JsonResponse({'error': str(e)}, status=500)
