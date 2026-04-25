
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

def edit_order(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = forms.ItemForm(instance=item)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if 'save_status' in request.POST and form.is_valid():
            item.current_item_status_date = timezone.now().date()
            item.save()
            return JsonResponse({'message': f'Item {item.tiptop_id} has been updated successfully.'})

    return render(request, 'your_template.html', {'form': form})
