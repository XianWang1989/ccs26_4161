
from django.http import JsonResponse

def your_view_name(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        if request.POST.get('status') == 'update':
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': f"Item {item.tiptop_id} status updated successfully."})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'message': "Item updated successfully."})

    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
