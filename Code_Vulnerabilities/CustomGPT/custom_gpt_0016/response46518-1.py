
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only use if CSRF token is not being handled, ensure to handle CSRF in production
def edit_order(request, order_id):
    item = get_object_or_404(Item, pk=order_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'message': "Form saved successfully."})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': "Status updated successfully."})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form, 'item': item})
