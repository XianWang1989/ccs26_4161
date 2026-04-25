
from allauth.account.forms import SignupForm
from django import forms

USER_TYPE_CHOICES = [
    ('architect', 'Architect'),
    ('client', 'Client'),
    # Add more user types as needed
]

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
