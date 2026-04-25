
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def update_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if 'save_status' in request.POST:
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})

    # Handle other form submissions if needed
