
# Override signup view
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        if self.request.user.user_type == 'architect':
            return '/architect-details/'  # Redirect to architect details
        return super().get_success_url()
