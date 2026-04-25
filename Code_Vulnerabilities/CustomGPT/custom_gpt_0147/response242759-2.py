
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[('architect', 'Architect'), ('designer', 'Designer')])

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

# In settings.py
ACCOUNT_SIGNUP_FORM_CLASS = 'yourapp.forms.CustomSignupForm'
