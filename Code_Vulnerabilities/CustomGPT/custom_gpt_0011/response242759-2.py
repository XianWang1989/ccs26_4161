
# forms.py

from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('client', 'Client'),
        ('architect', 'Architect'),
    ])

    def signup(self, request, user):
        user = super(CustomSignupForm, self).signup(request, user)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
