
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Item
from . import forms
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': f"Item {item.tiptop_id} status updated."})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': f"Item {item.tiptop_id} has been updated successfully."})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
