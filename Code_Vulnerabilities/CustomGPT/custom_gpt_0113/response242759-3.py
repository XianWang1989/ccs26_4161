
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('arch', 'Architect'), ('client', 'Client')])

    def signup(self, request, user):
        user = super().signup(request, user)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
