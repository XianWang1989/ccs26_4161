
from django.http import JsonResponse

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(
                message="Item {0} has been updated successfully.".format(item.tiptop_id)
            )
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'current_item_status_date': item.current_item_status_date.strftime('%Y-%m-%d')})

    return render(request, 'your_template.html', {'form': form, 'item': item})
