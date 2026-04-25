
import requests
from django.http import JsonResponse

def test_request_view(request):
    try:
        response = requests.post('http://example.com/api', data={'key': 'value'})
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.ConnectionError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
