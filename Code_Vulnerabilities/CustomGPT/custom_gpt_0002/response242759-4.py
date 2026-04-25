
# views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'arch':
                return redirect('architect_details_view')  # Redirect to business details form
            return redirect('home')  # Redirect to home for others
    else:
        form = CustomSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
