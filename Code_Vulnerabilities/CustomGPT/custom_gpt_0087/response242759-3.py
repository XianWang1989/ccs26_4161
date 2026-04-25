
from django.shortcuts import redirect
from django.urls import reverse

class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True
        user.save()

        if form.cleaned_data['user_type'] == 'architect':
            return redirect(reverse('architect_registration'))  # Redirect to the second step
        return complete_signup(self.request, user, self.get_success_url())
