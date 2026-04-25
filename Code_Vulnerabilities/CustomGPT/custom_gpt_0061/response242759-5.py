
# views.py
from django.shortcuts import render, redirect
from .forms import BusinessDetailsForm

def business_details_view(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Process the business details
            form.save()
            return redirect('home')  # Redirect to the desired page
    else:
        form = BusinessDetailsForm()
    return render(request, 'business_details.html', {'form': form})
