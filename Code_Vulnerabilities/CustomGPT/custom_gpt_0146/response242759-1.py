
# forms.py
from allauth.account.utils import complete_signup
from allauth.account.adapter import DefaultAccountAdapter
from django.utils import timezone

class CustomSignupForm(AccountAdapter):
    def send_confirmation_mail(self, request, user):
        user.is_active = True
        user.save()
        # Proceed with completion
        complete_signup(request, user)

# settings.py
ACCOUNT_SIGNUP_FORM_CLASS = 'path.to.CustomSignupForm'
