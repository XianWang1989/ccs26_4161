
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Item
from . import forms
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        if request.POST.get('save_item'):
            form = forms.ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
                return JsonResponse({"message": "Item updated."})
        elif request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({
                "message": "Status date updated.",
                "new_status": item.current_item_status_date.strftime("%Y-%m-%d")
            })
    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
