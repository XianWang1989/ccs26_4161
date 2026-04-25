
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ItemForm
from .models import Item
from datetime import date

def edit_order_view(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            if request.POST.get('save_status'):
                item.current_item_status_date = date.today()
                item.save()
                return JsonResponse({'message': "Item status updated successfully."})
            else:
                request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
                return JsonResponse({'message': "Item updated successfully."}, status=200)

    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_order.html', {'form': form, 'item': item})
