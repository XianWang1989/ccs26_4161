
from django.http import JsonResponse

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            # Handle the AJAX request separately
            if request.is_ajax():
                return JsonResponse({'message': 'Item updated successfully.'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            if request.is_ajax():
                return JsonResponse({'message': 'Status date updated successfully.'})

    # Add normal rendering logic for GET requests
    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form})
