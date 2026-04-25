
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # For simplicity in example, use CSRF tokens in production
def edit_order_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Status updated successfully!', 'status_date': item.current_item_status_date.isoformat()})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'message': "Item updated."})

    form = forms.ItemForm(instance=item)
    return render(request, 'edit_order.html', {'form': form, 'item': item})
