
from django.http import JsonResponse
from django.shortcuts import render
from datetime import date
from . import forms

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid() and request.POST.get('save_item'):
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'success': True})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': 'Status date updated.'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
