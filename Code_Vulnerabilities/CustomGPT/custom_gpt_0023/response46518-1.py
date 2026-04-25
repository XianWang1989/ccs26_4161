
from django.http import JsonResponse

def update_item_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': f"Item {item.tiptop_id} has been updated successfully."})
        else:
            return JsonResponse({'success': False, 'error': "Form is invalid."})

    return JsonResponse({'success': False, 'error': "Invalid request."})
