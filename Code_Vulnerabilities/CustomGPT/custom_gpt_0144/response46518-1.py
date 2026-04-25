from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from datetime import date
from .models import Item

def update_item_status(request, item_id):
    """
    View to update the item status date via AJAX.
    """
    if request.method == 'POST' and request.is_ajax():
        item = get_object_or_404(Item, pk=item_id)
        item.current_item_status_date = date.today()
        item.save()
        # Return the new date as a string so the client can update the UI
        return JsonResponse({
            'status': 'success',
            'current_item_status_date': item.current_item_status_date.strftime("%Y-%m-%d")
        })
    return JsonResponse({'status': 'failed'}, status=400)
