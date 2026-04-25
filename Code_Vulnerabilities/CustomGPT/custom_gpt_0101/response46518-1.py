
if request.method == 'POST':
    form = forms.ItemForm(request.POST, instance=item)
    if form.is_valid() and save_item is not None:
        form.save(True)
        request.user.message_set.create(message="Item {0} has been updated successfully.".format(item.tiptop_id))
        return JsonResponse({'status': 'success', 'message': 'Item updated.'})

    if request.POST.get('save_status'):
        item.current_item_status_date = date.today()
        item.save()
        return JsonResponse({'status': 'success', 'message': 'Status date updated.'})

return render(request, 'your_template.html', {'form': form})
