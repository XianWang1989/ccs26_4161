
form = UserForm(request.POST)
if form.is_valid():
    user = form.save()
else:
    errors = form.errors
