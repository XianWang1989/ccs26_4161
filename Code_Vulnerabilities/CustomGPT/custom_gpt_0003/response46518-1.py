
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item
from . import forms
from datetime import date

def edit_order_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and request.POST.get('save_item') is not None:
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
