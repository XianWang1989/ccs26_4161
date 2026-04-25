
import requests
from requests.exceptions import ConnectionError

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except ConnectionError as e:
        print("Connection Error:", e)
    except requests.HTTPError as e:
        print("HTTP Error:", e)

# Example usage in a Django view
from django.http import JsonResponse

def my_view(request):
    if request.method == 'POST':
        url = 'http://example.com/api/'
        data = {'key': 'value'}
        result = send_post_request(url, data)
        return JsonResponse(result)
