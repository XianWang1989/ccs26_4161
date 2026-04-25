
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use this for testing; ideally, implement CSRF protection
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save(True)
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))

            return JsonResponse({'status': "Item updated successfully."})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': "Status date updated successfully."})

    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
