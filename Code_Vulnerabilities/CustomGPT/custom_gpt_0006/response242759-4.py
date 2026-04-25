
# views.py

from django.shortcuts import redirect, render
from .forms import BusinessDetailsForm

def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'architect':
                return redirect('business_details')
            else:
                return redirect('home')  # or wherever you want to redirect

    else:
        form = CustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})

def business_details_view(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details
            return redirect('home')
    else:
        form = BusinessDetailsForm()
    return render(request, 'account/business_details.html', {'form': form})
