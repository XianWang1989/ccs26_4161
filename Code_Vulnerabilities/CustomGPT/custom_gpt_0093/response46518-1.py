
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item
from . import forms
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': f"Item {item.tiptop_id} has been updated successfully."
            })
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({
                'message': "Item status date updated successfully."
            })

    else:
        form = forms.ItemForm(instance=item)
    return render(request, 'edit_order.html', {'form': form, 'item': item})
