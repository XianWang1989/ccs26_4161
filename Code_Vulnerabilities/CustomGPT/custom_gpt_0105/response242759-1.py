
from allauth.account.utils import complete_signup
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import redirect
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def confirm_email(self, request, email_address):
        user = email_address.user
        user.is_active = True
        user.save()
        complete_signup(request, user, email_address)

    def get_success_url(self):
        return '/success/'
