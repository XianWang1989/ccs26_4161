
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import forms

@require_POST
def update_item_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Fetch your item model based on the provided ID
    if 'save_status' in request.POST:
        item.current_item_status_date = date.today()
        item.save()
        # Optionally, include additional data to return
        return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})
    return JsonResponse({'status': 'error', 'message': 'Failed to update status.'})
