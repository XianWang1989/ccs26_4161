
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailaddress):
        # Automatically confirm the user
        emailaddress.verified = True
        emailaddress.save()
        self.get_user(emailaddress).is_active = True
        self.get_user(emailaddress).save()
