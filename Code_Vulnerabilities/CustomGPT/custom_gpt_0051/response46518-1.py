
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

def edit_order(request, order_id):
    item = get_object_or_404(Item, id=order_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

            # Check if save_status was clicked
            if request.POST.get('save_status'):
                item.current_item_status_date = timezone.now()  # Update to current date and time
                item.save()
                return JsonResponse({'status': 'success', 'message': 'Status date updated'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
