
# forms.py
from allauth.account.forms import SignupForm
from django import forms

USER_TYPE_CHOICES = [
    ('architect', 'Architect'),
    ('client', 'Client'),
]

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']  # Assuming a user_type field exists
        user.save()
        return user
