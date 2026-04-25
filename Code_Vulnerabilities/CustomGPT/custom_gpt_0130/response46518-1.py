
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ItemForm
from .models import Item
from datetime import date

def edit_order(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)

        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully!'})

        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully!'})

    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
