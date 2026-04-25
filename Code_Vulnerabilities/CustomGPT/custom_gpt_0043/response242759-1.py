
# adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def send_confirmation_mail(self, request, emailconfirmation):
        # Instead of sending a confirmation mail, activate the user immediately
        emailconfirmation.confirm(self.request)
