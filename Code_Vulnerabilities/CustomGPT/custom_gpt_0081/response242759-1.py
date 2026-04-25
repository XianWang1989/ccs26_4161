
from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import gettext_lazy as _

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # You can customize your logic here, but returning True allows signup.
        return True

    def complete_signup(self, request, user, form, **kwargs):
        user.is_active = True  # Activate the user
        user.save()
        super().complete_signup(request, user, form, **kwargs)
