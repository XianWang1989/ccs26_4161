
from django.http import JsonResponse
from django.shortcuts import render

def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

            if request.POST.get('save_status'):
                item.current_item_status_date = date.today()
                item.save()
                return JsonResponse({'status': 'success', 'current_date': item.current_item_status_date.isoformat()})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
