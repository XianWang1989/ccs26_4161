
from django.http import JsonResponse
from django.shortcuts import render
from . import forms

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(instance=item)

    if request.method == 'POST':
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully'})

        # Handling form submission
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully'})

    return render(request, 'edit_order.html', {'form': form, 'item': item})
