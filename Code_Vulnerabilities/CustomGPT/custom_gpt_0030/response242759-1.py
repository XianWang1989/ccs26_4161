
# forms.py
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('regular', 'Regular User'),
        ('architect', 'Architect'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super().save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
