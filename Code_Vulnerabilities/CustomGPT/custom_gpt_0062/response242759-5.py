
# views.py
from django.shortcuts import render, redirect
from .forms import ArchitectDetailsForm

def architect_details_view(request):
    if request.method == 'POST':
        form = ArchitectDetailsForm(request.POST)
        if form.is_valid():
            # Save architect details
            form.save()
            return redirect('success_url')
    else:
        form = ArchitectDetailsForm()
    return render(request, 'architect_details.html', {'form': form})
