
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms

@csrf_exempt  # Use this for testing but consider CSRF protection in production
def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': "Item updated successfully."})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': "Status date updated."})

    form = forms.ItemForm(instance=item)
    return render(request, 'edit_order.html', {'form': form, 'item': item})
