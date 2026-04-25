
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def edit_order_view(request, order_id):
    item = get_object_or_404(Item, id=order_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and request.POST.get('save_item') is not None:
            form.save()
            return JsonResponse({'message': "Item updated successfully."})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': "Status date updated.", 'new_date': item.current_item_status_date.isoformat()})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
