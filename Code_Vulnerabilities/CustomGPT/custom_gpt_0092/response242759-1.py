
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate user
        user.save(using=self.get_user_model()._state.db)
        return super().save_user(request, user, form, commit)
