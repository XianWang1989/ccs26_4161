
from django.shortcuts import redirect
from django.urls import reverse

def custom_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'Architect':
                return redirect(reverse('business_details'))  # Redirect to business details
            return redirect('some-other-url')  # Normal redirect after signup
    else:
        form = CustomSignupForm()

    return render(request, 'account/signup.html', {'form': form})
