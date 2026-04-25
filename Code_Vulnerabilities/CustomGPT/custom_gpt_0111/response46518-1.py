
from django.http import JsonResponse

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            request.user.message_set.create(
                message=f"Item {item.tiptop_id} has been updated successfully."
            )
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated.'})

    return render(request, 'your_template.html', {'form': form, 'item': item})
