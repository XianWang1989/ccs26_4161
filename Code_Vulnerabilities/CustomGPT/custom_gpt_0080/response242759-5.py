
# views.py
from django.shortcuts import redirect
from django.urls import reverse

def custom_signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'architect':
                return redirect('architect_details')  # Redirect to architect form
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'your_template.html', {'form': form})
