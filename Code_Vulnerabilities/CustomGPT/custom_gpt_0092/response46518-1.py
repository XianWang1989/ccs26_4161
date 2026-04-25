
from django.http import JsonResponse
from django.shortcuts import render
from . import forms
from .models import Item

def edit_order(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully'})
        elif request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated successfully'})

    form = forms.ItemForm(instance=item)
    return render(request, 'edit_order.html', {'form': form, 'item': item})
