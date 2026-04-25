
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms

@csrf_exempt  # Use this only if you can't send CSRF token from JavaScript
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': f"Item {item.tiptop_id} status has been updated."})

    return JsonResponse({'message': 'Invalid form submission.'}, status=400)
