
import requests
from django.http import JsonResponse

def my_view(request):
    try:
        response = requests.post('http://external.server/endpoint', json={'key': 'value'})
        response.raise_for_status()  # Will raise an error for bad responses
    except requests.exceptions.RequestException as error:
        print("Error occurred: ", error)
        # Log the error or handle it further
        return JsonResponse({'error': str(error)}, status=500)

    return JsonResponse(response.json())
