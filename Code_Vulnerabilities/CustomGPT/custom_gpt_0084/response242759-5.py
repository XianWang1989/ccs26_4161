
# views.py
from django.shortcuts import render, redirect
from .forms import BusinessDetailsForm   # Your form for business details

def signup_complete(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Save the business details
            form.save()
            return redirect('success_url')  # Redirect after saving
    else:
        form = BusinessDetailsForm()
    return render(request, 'business_details.html', {'form': form})

# In your main signup view
def custom_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            # Check user type and redirect accordingly
            if user.user_type == 'Architect':
                return redirect('signup_complete')
            else:
                return redirect('success_url')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})
