
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.utils import timezone

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)

        # Activate the user
        self.user.is_active = True
        self.user.save()

        # Complete the signup process
        complete_signup(self.request, self.user, 'account/messages/signup.txt')

        return response
