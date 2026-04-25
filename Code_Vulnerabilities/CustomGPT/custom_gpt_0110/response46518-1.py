
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use cautiously; consider proper CSRF handling in production
def edit_order(request, order_id):
    item = get_object_or_404(Item, id=order_id)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated!'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success', 'message': 'Item updated successfully!'})

    # Handle GET request or other logic here
