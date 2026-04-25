
from django.http import JsonResponse
from django.shortcuts import render
from . import forms
from .models import Item
from datetime import date

def your_view_name(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid() and request.POST.get('save_item') is not None:
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'message': 'Item updated successfully.'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Item status updated successfully.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})  # Adjust your template name
