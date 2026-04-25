
from django.http import JsonResponse

def your_update_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        item.current_item_status_date = date.today()  # Update your status date
        item.save()
        return JsonResponse({'message': 'Item status updated successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
