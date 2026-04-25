
from django.http import JsonResponse
from datetime import date

def your_update_view(request):
    if request.method == 'POST' and request.is_ajax():
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)

        # Update the current item status date
        item.current_item_status_date = date.today()
        item.save()

        # Return a JSON response
        return JsonResponse({
            'new_status_date': item.current_item_status_date,
            'message': f"Item {item.tiptop_id} status updated successfully."
        })
