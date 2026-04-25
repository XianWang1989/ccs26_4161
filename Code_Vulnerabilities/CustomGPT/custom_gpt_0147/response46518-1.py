
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Handle CSRF for the sake of simplicity, but it's better to include CSRF token in AJAX
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST' and request.POST.get('status_update'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'updated_date': item.current_item_status_date})

    return JsonResponse({'error': 'Invalid request'}, status=400)
