
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def your_view_name(request):
    item = get_object_or_404(Item, id=request.POST.get('item_id'))

    if request.method == 'POST':
        if 'save_status' in request.POST:
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': f'Item {item.tiptop_id} status updated successfully.'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
