
# In your app's views.py
from django.shortcuts import redirect
from django.urls import reverse

def custom_signup_view(request):
    if request.method == 'POST':
        # process the form
        user_type = request.POST.get('user_type')
        if user_type == 'architect':
            return redirect(reverse('architect_details'))  # Point to your architect details page
    return redirect('some_default_page')  # Default redirect if conditions are not met
