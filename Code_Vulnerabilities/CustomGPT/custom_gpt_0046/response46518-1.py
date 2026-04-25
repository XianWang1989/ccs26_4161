
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item
from . import forms
from datetime import date

def edit_order(request, item_id):
    item = Item.objects.get(id=item_id)  # Get the item based on ID
    form = forms.ItemForm(instance=item)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            message = f"Item {item.tiptop_id} has been updated successfully."
            request.user.message_set.create(message=message)
            return JsonResponse({'message': message, 'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Status updated successfully!', 'status': 'success'})

    return render(request, 'your_template.html', {'form': form, 'item': item})
