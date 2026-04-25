
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only use this for testing; it's better to use CSRF tokens in production
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated!'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Item has been updated successfully.'})

    form = forms.ItemForm(instance=item)
    return render(request, 'edit_order.html', {'form': form, 'item': item})
