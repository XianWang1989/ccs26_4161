
import requests
from django.http import JsonResponse

def my_view(request):
    if request.method == "POST":
        try:
            # Example external URL
            url = "http://external-server/api/"
            payload = {'key': 'value'}
            response = requests.post(url, json=payload)

            # Check if the request was successful
            response.raise_for_status()
            return JsonResponse(response.json())

        except requests.ConnectionError as e:
            return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Send a POST request'}, status=200)
