
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('Architect', 'Architect'),
        ('Client', 'Client'),
    ])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

# In your settings.py
ACCOUNT_SIGNUP_FORM_CLASS = 'path.to.your.CustomSignupForm'
