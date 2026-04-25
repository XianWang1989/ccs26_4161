
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('arch', 'Architect'), ('client', 'Client')])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user
