
# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('Architect', 'Architect'),
        ('Other', 'Other')
    ])

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
