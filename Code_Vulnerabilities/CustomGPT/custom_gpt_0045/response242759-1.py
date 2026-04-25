
# myapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        # Override to skip sending confirmation emails
        pass

    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, *args, **kwargs):
        user.is_active = True  # Automatically activate the user
        super(MyAccountAdapter, self).save_user(request, user, form, *args, **kwargs)
