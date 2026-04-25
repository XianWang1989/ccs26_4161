
from django.http import JsonResponse
import requests

def my_view(request):
    if request.method == 'POST':
        try:
            response = requests.post('http://<IPv4-address>/api/endpoint', data={'key': 'value'})
            return JsonResponse({'status': 'success', 'data': response.json()})
        except requests.ConnectionError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
