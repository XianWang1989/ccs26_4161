
from django.http import JsonResponse

if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status date updated successfully.'})

    # other logic...

return render(request, 'your_template.html', {'form': form, 'item': item})
