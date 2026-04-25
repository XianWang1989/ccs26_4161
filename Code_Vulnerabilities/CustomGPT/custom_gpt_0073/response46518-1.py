
from django.http import JsonResponse
from django.shortcuts import render

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(instance=item)

    if request.method == 'POST':
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({
                'status': 'success',
                'message': f"Item {item.tiptop_id} status updated."
            })
        else:
            form = forms.ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return JsonResponse({
                    'status': 'success',
                    'message': f"Item {item.tiptop_id} has been updated successfully."
                })

    return render(request, 'edit_order.html', {'form': form, 'item': item})
