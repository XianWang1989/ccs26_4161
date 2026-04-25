
from django.http import JsonResponse
from django.shortcuts import render
from . import forms

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and 'save_item' in request.POST:
            form.save()
            message = f"Item {item.tiptop_id} has been updated successfully."
            return JsonResponse({'status': 'success', 'message': message})

        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
