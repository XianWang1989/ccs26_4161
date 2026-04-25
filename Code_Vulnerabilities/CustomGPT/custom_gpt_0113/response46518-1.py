
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

@csrf_exempt  # Only for development; use CSRF tokens in production
def edit_order(request, order_id):
    item = get_object_or_404(Item, id=order_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save(commit=True)
            request.user.message_set.create(message=f"Item {item.tiptop_id} has been updated successfully.")
            return JsonResponse({'status': 'success'})

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'status_updated'})

    else:
        form = forms.ItemForm(instance=item)

    return render(request, 'your_template.html', {'form': form})
