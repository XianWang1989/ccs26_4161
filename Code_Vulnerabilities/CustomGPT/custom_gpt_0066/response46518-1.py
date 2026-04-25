
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # If you're using this for testing; consider using proper CSRF protection in production.
def your_view_name(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        if request.POST.get('save_status'):
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({'status': 'success'})

        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
            return JsonResponse({'status': 'form_saved'})

    form = forms.ItemForm(instance=item)
    return render(request, 'your_template.html', {'form': form, 'item': item})
