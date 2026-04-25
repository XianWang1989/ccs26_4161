
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Handle CSRF token if necessary
def update_item_status(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        item.current_item_status_date = date.today()
        item.save()
        message = f"Item {item.tiptop_id} status has been updated successfully."
        return JsonResponse({'message': message})

    return JsonResponse({'error': 'Invalid request'}, status=400)
