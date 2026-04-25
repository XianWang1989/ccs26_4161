
# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BusinessDetailsForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if form.cleaned_data['user_type'] == 'Architect':
                return redirect('business_details')  # Redirect to additional form
            return redirect('home')  # Or wherever else
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})

def business_details_view(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save business details logic here
            return redirect('home')
    else:
        form = BusinessDetailsForm()
    return render(request, 'business_details.html', {'form': form})

# urls.py
from django.urls import path
from .views import signup_view, business_details_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('business-details/', business_details_view, name='business_details'),
]
