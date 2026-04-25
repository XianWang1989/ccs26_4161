
from django.http import JsonResponse
from django.shortcuts import render
from . import forms

def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            # Update current item status date
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': 'Status updated successfully!'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': f'Item {item.tiptop_id} has been updated successfully!'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
