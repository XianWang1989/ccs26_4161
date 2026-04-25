
# forms.py
from allauth.account.adapter import get_adapter
from allauth.account.utils import complete_signup
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    # Add your custom fields
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('other', 'Other')])

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
