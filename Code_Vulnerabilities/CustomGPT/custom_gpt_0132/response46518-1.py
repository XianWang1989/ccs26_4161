
from django.http import JsonResponse
from django.shortcuts import render

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status_saved', 'current_date': item.current_item_status_date.isoformat()})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
