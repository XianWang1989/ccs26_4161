
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Or use a better approach to allow CSRF
def update_item_status(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'message': f'Item {item.tiptop_id} status updated successfully.'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
