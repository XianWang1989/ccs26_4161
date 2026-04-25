
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def user_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'Architect':
                return redirect('architect_details')  # redirect to specific details page
            return redirect('home')
