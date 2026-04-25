
from django.shortcuts import redirect
from django.urls import reverse

def custom_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'architect':
                return redirect(reverse('architect_details'))  # Ensure you have a URL for this
            return redirect(reverse('home'))
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})
