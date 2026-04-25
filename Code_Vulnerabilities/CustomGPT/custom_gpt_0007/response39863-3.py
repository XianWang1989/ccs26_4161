
def my_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Process the valid email
    else:
        form = EmailForm()

    return render(request, 'my_template.html', {'form': form})
