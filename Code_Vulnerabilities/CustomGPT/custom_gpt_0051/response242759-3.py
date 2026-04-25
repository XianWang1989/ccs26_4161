
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def post_signup_redirect(request):
    if request.user.user_type == 'Architect':
        return redirect(reverse('architect_details'))  # Your details page URL
    return redirect(reverse('home'))  # Default home URL

# In your signup view, you might include:
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            return post_signup_redirect(request)
