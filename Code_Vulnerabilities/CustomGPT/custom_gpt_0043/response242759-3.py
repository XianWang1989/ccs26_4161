
# forms.py

from allauth.account.forms import SignupForm
from django import forms

USER_TYPE_CHOICES = [
    ('Architect', 'Architect'),
    ('Client', 'Client'),
    # Add other user types here
]

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
