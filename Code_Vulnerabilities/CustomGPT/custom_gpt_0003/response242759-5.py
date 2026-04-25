
# myapp/views.py
from django.shortcuts import render, redirect
from .models import UserDetails  # Assume you have a model for storing additional data
from .forms import BusinessDetailsForm

def business_details(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save the data and redirect
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect('home')  # Redirect to the desired page
    else:
        form = BusinessDetailsForm()
    return render(request, 'myapp/business_details.html', {'form': form})
