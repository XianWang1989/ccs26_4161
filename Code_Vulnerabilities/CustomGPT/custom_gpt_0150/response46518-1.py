
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def your_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item has been updated successfully.")

            if request.POST.get('save_status'):
                item.current_item_status_date = date.today()
                item.save()

            return JsonResponse({'status': 'success'})

    return render(request, 'your_template.html', {'form': form, 'item': item})
