
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def update_item_status(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})

    return JsonResponse({'success': False, 'message': 'Failed to update status.'})
