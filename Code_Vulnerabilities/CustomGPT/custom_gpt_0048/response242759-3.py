
# your_app/forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('architect', 'Architect'),
        ('client', 'Client'),
        # Add more user types as needed
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

    def save(self, request):
        # Save the user and user type
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']  # Make sure to add this field to your User model
        user.save()
        return user
