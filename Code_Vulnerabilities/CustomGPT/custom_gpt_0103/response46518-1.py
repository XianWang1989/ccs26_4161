
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def your_view_name(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(id=item_id)

        if request.POST.get('status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'new_status_date': item.current_item_status_date})

    # Handle other POST logic if needed
