
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use this only for testing; implement proper CSRF protection in production
def update_item_status(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(id=item_id)  # Replace Item with your model name

        item.current_item_status_date = date.today()
        item.save()

        return JsonResponse({'message': f'Item {item.tiptop_id} status updated successfully.'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
