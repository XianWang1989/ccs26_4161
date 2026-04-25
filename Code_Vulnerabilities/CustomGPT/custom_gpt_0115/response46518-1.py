
from django.http import JsonResponse
from django.shortcuts import render
from . import forms
from .models import Item
from datetime import date

def edit_order(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item has been updated successfully.")
            return JsonResponse({"message": "Item updated.", "status": "success"})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({"message": "Status date updated.", "status": "success"})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
