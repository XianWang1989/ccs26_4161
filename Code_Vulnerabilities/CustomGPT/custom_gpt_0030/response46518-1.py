
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})

        # Handle form submission here
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': f'Item {item.tiptop_id} has been updated successfully.'})

    # If not a post request, display the form
    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
