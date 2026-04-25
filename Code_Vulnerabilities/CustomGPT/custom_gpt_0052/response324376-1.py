
import requests
from django.http import JsonResponse

def test_post(request):
    try:
        response = requests.post('http://external-server/api/', data={'key': 'value'})
        return JsonResponse({'status': 'success', 'data': response.json()})
    except requests.ConnectionError as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
