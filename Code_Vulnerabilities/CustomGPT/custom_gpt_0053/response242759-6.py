
# adapters.py
from allauth.account.utils import complete_signup

class MyAccountAdapter(DefaultAccountAdapter):
    # ...
    def get_signup_redirect_url(self, request):
        user = request.user
        if user.user_type == 'Architect':
            return '/architect-registration/'  # URL of your architect registration view
        return super().get_signup_redirect_url(request)
