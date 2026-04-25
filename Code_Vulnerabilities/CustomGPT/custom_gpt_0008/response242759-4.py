
# views.py
from django.shortcuts import render, redirect
from .forms import BusinessDetailsForm

def signup_complete(request):
    if request.method == 'POST':
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            # Process the business details
            form.save()
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = BusinessDetailsForm()

    return render(request, 'business_details.html', {'form': form})

# Add the route to your urls.py
urlpatterns = [
    path('signup/complete/', signup_complete, name='signup_complete'),
]
