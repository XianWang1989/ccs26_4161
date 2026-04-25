
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_item_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.current_item_status_date = date.today()
        item.save()
        response = {
            'status': 'success',
            'message': f'Item {item.tiptop_id} status updated successfully.'
        }
        return JsonResponse(response)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
