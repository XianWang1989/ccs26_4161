
from allauth.account.adapter import get_adapter
from allauth.account.utils import complete_signup

class CustomSignupView(SignupView):
    def perform_create(self, serializer):
        user = serializer.save(self.request)
        user.is_active = True  # Automatically activate the user
        user.save()
        # Redirect after signup
        complete_signup(self.request, user, self.get_success_url())

