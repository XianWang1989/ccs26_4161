
from django.http import JsonResponse

def edit_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = forms.ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'success': True, 'message': "Item updated successfully."})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'template.html', {'form': form, 'item': item})
