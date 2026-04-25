
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item
from . import forms
from datetime import date

def edit_order_view(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'success'}, status=200)

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status updated'}, status=200)

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
