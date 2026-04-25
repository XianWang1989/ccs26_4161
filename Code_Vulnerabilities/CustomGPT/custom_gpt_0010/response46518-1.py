
from django.http import JsonResponse

def your_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'success': True})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'updated_date': item.current_item_status_date.strftime('%Y-%m-%d')})

    # Handle GET or other methods here
