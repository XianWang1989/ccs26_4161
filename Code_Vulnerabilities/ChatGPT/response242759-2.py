
# forms.py

from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    USER_TYPES = [
        ('architect', 'Architect'),
        ('client', 'Client'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPES, label="User Type")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
