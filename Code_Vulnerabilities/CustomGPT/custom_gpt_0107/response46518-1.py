
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yourapp.models import Item  # Adjust import based on your project structure

@csrf_exempt  # Use this to exempt CSRF check for simplicity. Use with caution.
def update_item_status(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
