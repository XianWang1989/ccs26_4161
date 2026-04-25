
from django.http import JsonResponse

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            message = "Item {0} has been updated successfully.".format(item.tiptop_id)
            return JsonResponse({'status': 'success', 'message': message})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
