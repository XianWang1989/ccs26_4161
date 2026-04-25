
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def update_item_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})

    # Handle other form submissions if needed
    else:
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

    return JsonResponse({'status': 'error', 'message': 'Failed to update.'})
