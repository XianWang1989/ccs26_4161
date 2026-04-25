
from django.http import JsonResponse
from django.shortcuts import render
from . import forms  # Assuming your form is in this module
from datetime import date

def edit_order_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            message = "Item {0} has been updated successfully.".format(item.tiptop_id)
            request.user.message_set.create(message=message)

            # Check if save_status was pressed
            if request.POST.get('save_status'):
                item.current_item_status_date = date.today()
                item.save()
                return JsonResponse({'message': message, 'status_date': item.current_item_status_date.strftime('%Y-%m-%d')})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
