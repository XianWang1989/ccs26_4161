
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use cautiously in production
def your_view_name(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        form = forms.ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            item.current_item_status_date = date.today()
            item.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    # Handle GET requests if needed
    return render(request, 'your_template.html', {'form': form})
