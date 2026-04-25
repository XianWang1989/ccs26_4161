
# views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

class CustomSignupView(View):
    def get(self, request):
        signup_form = CustomSignupForm()
        return render(request, 'account/signup.html', {'form': signup_form})

    def post(self, request):
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            if user.user_type == 'Architect':
                return redirect(reverse('architect_details')) # Redirect to architect details
            return redirect('next_step')  # Redirect to the default next step
        return render(request, 'account/signup.html', {'form': form})
