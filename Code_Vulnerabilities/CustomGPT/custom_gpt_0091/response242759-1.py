
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.utils.http import url_has_allowed_host_and_scheme

class CustomSignupView(SignupView):

    def form_valid(self, form):
        # Automatically activate user
        user = form.save(self.request)
        user.is_active = True
        user.save()
        return complete_signup(self.request, user, self.get_success_url())
