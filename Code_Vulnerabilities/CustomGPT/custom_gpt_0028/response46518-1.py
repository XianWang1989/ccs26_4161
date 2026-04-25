
from django.http import JsonResponse
from django.shortcuts import render
from datetime import date

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)  # Assuming Item is your model

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'new_status_date': item.current_item_status_date.strftime('%Y-%m-%d')})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
