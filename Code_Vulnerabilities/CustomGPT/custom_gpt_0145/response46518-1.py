
from django.http import JsonResponse

def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and save_item is not None:
            form.save()
            message = "Item {0} has been updated successfully.".format(item.tiptop_id)
            request.user.message_set.create(message=message)
            return JsonResponse({'message': message, 'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Status date updated successfully.', 'status': 'success'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
