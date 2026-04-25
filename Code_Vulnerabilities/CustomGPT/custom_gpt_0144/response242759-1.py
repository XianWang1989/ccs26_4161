# forms.py
from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('architect', 'Architect'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def save(self, request):
        user = super().save(request)
        user.profile.user_type = self.cleaned_data['user_type']
        user.profile.save()
        return user
