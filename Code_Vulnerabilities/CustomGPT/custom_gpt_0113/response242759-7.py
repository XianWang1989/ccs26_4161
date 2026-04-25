
from django.shortcuts import render

def architect_details_view(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Save form data to the user model or a separate model
            return redirect('success_page')
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
