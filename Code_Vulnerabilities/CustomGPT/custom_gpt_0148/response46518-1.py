
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Item
from . import forms
from datetime import date

@require_POST
def edit_order(request, item_id):
    item = Item.objects.get(pk=item_id)  # Get the item by ID
    form = forms.ItemForm(request.POST, instance=item)

    if form.is_valid():
        form.save()
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
        return JsonResponse({'status': 'success', 'message': 'Item updated.'})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'status': 'success', 'message': 'Status date updated.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid data.'})
