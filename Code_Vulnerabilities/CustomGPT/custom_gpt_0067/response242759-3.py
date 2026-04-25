
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('architect', 'Architect'),
        ('builder', 'Builder'),
        ('client', 'Client'),
    ])

    def signup(self, request, user):
        user_type = self.cleaned_data['user_type']
        user.user_type = user_type  # Assuming you have a user_type field in your User model
        user.save()
        return super().signup(request, user)
