
from django.http import JsonResponse
from django.shortcuts import render

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = "Item {0} has been updated successfully.".format(item.tiptop_id)
            return JsonResponse({'success': True, 'message': message})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': "Status updated successfully."})

    return render(request, 'edit_order.html', {'form': form, 'item': item})
