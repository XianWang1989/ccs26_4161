
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use with caution. Consider implementing CSRF tokens for security.
def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': "Status updated."})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': "Item updated successfully."})

    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
