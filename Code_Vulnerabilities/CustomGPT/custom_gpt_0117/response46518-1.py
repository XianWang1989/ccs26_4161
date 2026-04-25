
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Item
from . import forms
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': f"Item {item.tiptop_id} has been updated successfully."})

        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status updated', 'date': item.current_item_status_date.isoformat()})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
