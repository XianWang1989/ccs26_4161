
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Activate the user immediately
        user.save()
        return user
