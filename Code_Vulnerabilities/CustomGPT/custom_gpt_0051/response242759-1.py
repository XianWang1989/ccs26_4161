
# forms.py
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('Architect', 'Architect'),
        ('Client', 'Client'),
    ])

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
