
from django.http import JsonResponse

def check_file_view(request):
    url = request.GET.get('url')  # Assuming you pass the URL as a query parameter
    exists = check_file_exists(url)
    return JsonResponse({'exists': exists})
