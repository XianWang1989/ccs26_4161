
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'success': True, 'message': f'Item {item.tiptop_id} status updated.'})

    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': f'Item {item.tiptop_id} has been updated successfully.'})

    return JsonResponse({'success': False, 'errors': form.errors})
