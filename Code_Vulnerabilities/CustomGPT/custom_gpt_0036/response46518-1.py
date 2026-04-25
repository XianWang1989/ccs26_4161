
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from . import forms
from .models import Item

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(instance=item)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': f'Item {item.tiptop_id} status updated!'})
        else:
            form = forms.ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success', 'message': f'Item {item.tiptop_id} has been updated successfully.'})

    return render(request, 'edit_order.html', {'form': form, 'item': item})
