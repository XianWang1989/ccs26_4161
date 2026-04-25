
from django.http import JsonResponse
from django.shortcuts import render
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Retrieve the item

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status_updated', 'date': item.current_item_status_date.isoformat()})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
