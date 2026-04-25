
# In your app's adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        super(MyAccountAdapter, self).save_user(request, user, form, commit)
        user.is_active = True
        user.save()
