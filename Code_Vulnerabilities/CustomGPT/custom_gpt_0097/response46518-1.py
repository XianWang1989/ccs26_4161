
from django.http import JsonResponse

def your_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        if request.POST.get('save_item'):
            form = forms.ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                # Other logic...

        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'message': f'Item {item.tiptop_id} status updated successfully.'})

    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
