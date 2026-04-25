
from django.http import JsonResponse
from django.shortcuts import render
from . import forms

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            # Update current item status date
            if request.POST.get('save_status'):
                item.current_item_status_date = date.today()
                item.save()
                # Respond to AJAX with success message
                return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})

            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success', 'message': 'Form saved.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form})
