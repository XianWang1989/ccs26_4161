
from django.shortcuts import redirect

class CustomSignupView(SignupView):

    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = True
        user.save()

        # Redirect based on user type
        if user.user_type == 'architect':
            return redirect('architect_details')
        return redirect('home')
