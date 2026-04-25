
from django.http import JsonResponse
from django.shortcuts import render

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        if request.POST.get('action') == 'save_status':
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': f'Item {item.tiptop_id} status updated.'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
