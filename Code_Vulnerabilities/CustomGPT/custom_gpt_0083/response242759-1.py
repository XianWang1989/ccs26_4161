
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(
        choices=[
            ('Architect', 'Architect'),
            ('OtherType', 'OtherType'),
        ],
        required=True
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Activate user
        user.save()
        return user
