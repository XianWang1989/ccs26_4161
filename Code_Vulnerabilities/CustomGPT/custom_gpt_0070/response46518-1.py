
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use with caution; better to handle CSRF properly
def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': f'Item {item.tiptop_id} status updated.'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'message': f'Item {item.tiptop_id} updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
