
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from django.utils.translation import ugettext_lazy as _

class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Activate the user immediately
        user = form.save(self.request)
        user.is_active = True
        user.save()
        return complete_signup(self.request, user, self.get_success_url())
