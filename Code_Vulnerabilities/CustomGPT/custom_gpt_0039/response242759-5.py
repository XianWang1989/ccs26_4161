
# views.py
from django.shortcuts import render, redirect
from .forms import BusinessDetailsForm  # Create this form for business details

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            request.session['user_type'] = form.cleaned_data['user_type']
            if user.user_type == 'architect':
                return redirect('business_details')  # Redirect to business details form
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})

def business_details_view(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details here
            return redirect('home')
    else:
        form = BusinessDetailsForm()
    return render(request, 'account/business_details.html', {'form': form})
