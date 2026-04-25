
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only if you want to bypass CSRF for AJAX (not recommended)
def your_view_name(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)

        if request.POST.get('status') == 'save_status':
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Status updated successfully.'})

        # Handle regular form submission if needed
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Item updated successfully.'})

    # Handle GET requests or other methods
    ...
