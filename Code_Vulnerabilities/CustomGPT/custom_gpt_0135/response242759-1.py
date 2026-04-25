
# forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile  # Assuming you have a UserProfile model

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[
        ('Architect', 'Architect'),
        ('Engineer', 'Engineer'),
        # Add other user types
    ])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        return user
