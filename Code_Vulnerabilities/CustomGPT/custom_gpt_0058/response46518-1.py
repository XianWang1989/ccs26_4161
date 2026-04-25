
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

@csrf_exempt  # Use with caution, ensure CSRF protection in production environments
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Update the current item status date
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': 'Item has been updated successfully.'})

    # Add logic for GET request if needed...
