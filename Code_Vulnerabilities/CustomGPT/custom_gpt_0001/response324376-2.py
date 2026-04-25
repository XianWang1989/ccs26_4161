
import requests
from django.http import JsonResponse
from requests.exceptions import ConnectionError

def post_data_view(request):
    if request.method == 'POST':
        url = "http://example.com/api/endpoint"
        try:
            response = requests.post(url, json={'key': 'value'})
            response.raise_for_status()  # Raises HTTPError for bad responses
            return JsonResponse({'status': 'success', 'data': response.json()})
        except ConnectionError as e:
            return JsonResponse({'status': 'error', 'message': f"Connection error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"An error occurred: {str(e)}"}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
