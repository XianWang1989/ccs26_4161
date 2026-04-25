
import requests
from django.http import JsonResponse

def my_view(request):
    if request.method == 'POST':
        url = 'https://external.server/api/endpoint'  # replace with your URL
        data = {'key': 'value'}

        try:
            # Submit POST request
            response = requests.post(url, json=data)
            response.raise_for_status()  # raises an HTTPError for bad responses

            return JsonResponse({'status': 'success', 'data': response.json()})

        except requests.exceptions.RequestException as e:
            # Handle the exception raised by requests
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
