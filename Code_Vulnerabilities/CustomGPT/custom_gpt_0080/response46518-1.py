
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt  # Only use if CSRF is properly managed in other ways.
def update_item_status(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.current_item_status_date = timezone.now()
        item.save()

        return JsonResponse({'message': f'Item status updated to {item.current_item_status_date}.'})
