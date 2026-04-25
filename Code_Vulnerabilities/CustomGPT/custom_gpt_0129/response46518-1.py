
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

@csrf_exempt  # Only if you're not using CSRF tokens in AJAX
def update_item_status(request, item_id):
    item = get_object_or_404(ItemModel, pk=item_id)
    if request.method == 'POST':
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Item status date updated successfully.',
            'current_date': item.current_item_status_date.strftime('%Y-%m-%d')
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
